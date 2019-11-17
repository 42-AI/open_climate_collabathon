import pandas as pd
import matplotlib.pyplot as plt


def _load_pledge_data(scenario):
    def extract_pledge_data(xls, sheet, country='USA'):
        df = pd.read_excel(xls, sheet_name=sheet, header=1, index_col=0)
        country_label = "'" + country + "'"
        df = df.loc[country_label, :]
        df = df / 1000000  # Convert units: Gg to Gt
        return df

    sheets = {
        '1.5C' : 'CBDR-RC hybrid 1.5°C-scenario',
        '2.0C' : 'CBDR-RC hybrid 2°C-scenario'

    }
    xls = pd.ExcelFile('data/Data Pledged Warming Map.xlsx')
    pledge_data = extract_pledge_data(xls, sheets[scenario])
    return pledge_data

'''Returns proportion of national historical population for each state'''
def _load_hist_population_data():
    pop_hist = pd.read_excel('data/population.xls', header=1, index_col=0)
    pop_hist = pop_hist.loc[:,[2015,2010,2000,1990]]
    pop_hist_prop = pop_hist / pop_hist.loc['Total U.S.']
    return pop_hist_prop

'''Returns proportion of national projected population for each state'''
def _load_proj_population_data():
    pop_proj = pd.read_excel('data/NationalProjections_ProjectedTotalPopulation_2020-2040_Updated12-2018.xls',
                         header=3, index_col=1, skipfooter=1)
    pop_proj.drop(['Unnamed: 0',2010], axis=1, inplace=True)
    pop_proj_prop = pop_proj / pop_proj.loc['United States']
    pop_proj_prop.rename(index={'United States':'Total U.S.'}, inplace=True)
    return pop_proj_prop



'''
Returns a pandas Dataframe conaining a table ready for plotting
The data represents state GHG emissions allocations under the CBDR-RC hybrid 1.5°C/2.0°C-scenarios [in GtCO2eq]
The years represented are 1990-2040
The scenario argument (string format) specifies for which scenario to output the state budgets: +-
"1.5C" and "2.0C"
'''
def get_data(scenario):

    pledge_data = _load_pledge_data(scenario)
    pop_hist_data = _load_hist_population_data()
    pop_proj_data = _load_proj_population_data()

    data = pd.DataFrame(index=pop_hist_data.index, columns=range(1990,2041), dtype=float)
    data.loc[:,pop_hist_data.columns] = pop_hist_data
    data.loc[:,pop_proj_data.columns] = pop_proj_data

    data.interpolate(axis=1, inplace=True)

    return data.multiply(pledge_data.loc[data.columns], axis=1)