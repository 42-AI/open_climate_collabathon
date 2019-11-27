import pandas as pd


def _load_pledge_data(data_file, country, scenario):
    def extract_pledge_data(xls, sheet, country):
        df = pd.read_excel(xls, sheet_name=sheet, header=1, index_col=0)
        country_label = "'" + country + "'"
        df = df.loc[country_label, :]
        df = df / 1000000  # Convert units: Gg to Gt
        return df

    sheets = {
        '1.5C' : 'CBDR-RC hybrid 1.5°C-scenario',
        '2.0C' : 'CBDR-RC hybrid 2°C-scenario'

    }
    xls = pd.ExcelFile(data_file)
    pledge_data = extract_pledge_data(xls, sheets[scenario], country)
    return pledge_data

'''Returns proportion of national historical population for each state'''
def _load_population_data(data_file):
    pop = pd.read_excel(data_file, header=0, index_col=0)
    pop_states = pop.loc[:, pop.columns[1:]]
    pop_prop = pop_states / pop.loc['Total']
    return pop_prop


'''
Returns a pandas Dataframe conaining a table ready for plotting
The data represents state GHG emissions allocations under the CBDR-RC hybrid 1.5°C/2.0°C-scenarios [in GtCO2eq]
The years represented are 1990-2040
The scenario argument (string format) specifies for which scenario to output the state budgets: +-
"1.5C" and "2.0C"
'''
def get_data(pledged_data="media/data/Data_Pledged_Warming_Map.xlsx", data_file="", country="", scenario="1.5C"):

    pledge_data = _load_pledge_data(pledged_data, country, scenario)
    pop_data = _load_population_data(data_file)

    data = pd.DataFrame(index=pop_data.index, columns=range(1990,2041), dtype=float)
    data.loc[:,pop_data.columns] = pop_data

    data.interpolate(axis=1, inplace=True)

    return data.multiply(pledge_data.reindex(data.columns), axis=1)

if __name__ == "__main__":
    data = get_data(pledged_data="../media/data/Data_Pledged_Warming_Map.xlsx", data_file="../media/data/Populations_USA.xlsx", country="USA")
    print(data.head)
