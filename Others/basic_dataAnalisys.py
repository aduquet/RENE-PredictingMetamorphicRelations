from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import collections

fsize = 12
tsize = 12
tdir = 'in'
major = 5.0
minor = 3.0

style = 'default'
plt.style.use(style)
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = fsize
plt.rcParams['legend.fontsize'] = tsize
plt.rcParams['xtick.direction'] = tdir
plt.rcParams['ytick.direction'] = tdir
plt.rcParams['xtick.major.size'] = major
plt.rcParams['xtick.minor.size'] = minor
plt.rcParams['ytick.major.size'] = major
plt.rcParams['ytick.minor.size'] = minor
plt.rcParams["figure.figsize"] = (6, 6)
plt.rcParams['legend.handlelength'] = 0.5


def def_plot(df):

    add_1 = df['ADD'].value_counts()[1]
    add_0 = df['ADD'].value_counts()[0]

    mul_1 = df['MUL'].value_counts()[1]
    mul_0 = df['MUL'].value_counts()[0]

    per_1 = df['PER'].value_counts()[1]
    per_0 = df['PER'].value_counts()[0]

    inc_1 = df['INC'].value_counts()[1]
    inc_0 = df['INC'].value_counts()[0]

    exc_1 = df['EXC'].value_counts()[1]
    exc_0 = df['EXC'].value_counts()[0]

    inv_1 = df['INV'].value_counts()[1]
    inv_0 = df['INV'].value_counts()[0]

    colors = ['#3e5683', '#6b7c82', '#6a9b62', '#a18abf', '#985399', '#93003a']
    names = ['ADD', 'MUL', 'PER', 'INC', 'EXC', 'INV']

    uno = [add_1, mul_1, per_1, inc_1, exc_1, inv_1]
    cero =[add_0, mul_0, per_0, inc_0, exc_0, inv_0]

    d = {'MR': names, 'freq_1': uno, 'freq_0': cero}
    df = pd.DataFrame(data=d, index=None)
    df.to_csv('MRsFrec.csv')

    ax = plt.figure
    ax = df.plot.bar(stacked=True, color=['#565656', '#720022'])
    ax.set_xticklabels(names)

    plt.xlabel("Metamorphic relations")
    plt.ylabel("Number of Methods")
    plt.legend(('Does satisfy','Does not satisfy'), fancybox=True, shadow=True, ncol=2,  bbox_to_anchor=(0.5, 1.05), loc='upper center')
    plt.savefig("Total number of methods that satisfies or non-satisfies each metamorphic relation.pdf")
    plt.show()

def counter_MRs(df):
    aux = []

    methodName_aux_0 = []
    methodName_aux_1 = []
    methodName_aux_2 = []
    methodName_aux_3 = []
    methodName_aux_4 = []
    methodName_aux_5 = []
    methodName_aux_6 = []

    ds_aux = []
    mrs_name = ['ADD', 'MUL', 'PER', 'INC', 'EXC', 'INV']
    for i in range(0, len(mrs_name) + 1):
        df_aux= {'Num_MRs': i , 'methodName': 'a', 'Total methods': 0, 'Total_MRs':0, 'ADD':0, 'MUL':0, 'PER':0, 'INC':0, 'EXC':0, 'INV':0}
        ds_aux.append(df_aux)
    df2 = pd.DataFrame(ds_aux)

    for index, row in df.iterrows():
        add = row.at['ADD']
        mul = row.at['MUL']
        per = row.at['PER']
        inc = row.at['INC']
        exc = row.at['EXC']
        inv = row.at['INV']

        mrs = [add, mul, per, inc, exc, inv]
        
        aux.append(sum(mrs))

        if sum(mrs) == 0:
            methodName_aux_0.append(row.at['Method Name'])
            df2.at[0,'methodName'] = methodName_aux_0
            df2.at[0,'Total methods'] =len(methodName_aux_0)
            
        if sum(mrs) == 1:
            methodName_aux_1.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[1, mrn] = df2.at[1, mrn] + 1
            df2.at[1,'methodName'] = methodName_aux_1
            df2.at[1,'Total methods'] =len(methodName_aux_1)

        if sum(mrs) == 2:
            methodName_aux_2.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[2, mrn] = df2.at[2, mrn] + 1
            df2.at[2,'methodName'] = methodName_aux_2
            df2.at[2,'Total methods'] =len(methodName_aux_2)

        if sum(mrs) == 3:
            methodName_aux_3.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[3, mrn] = df2.at[3, mrn] + 1
            df2.at[3,'methodName'] = methodName_aux_3
            df2.at[3,'Total methods'] =len(methodName_aux_3)

        if sum(mrs) == 4:
            methodName_aux_4.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[4, mrn] = df2.at[4, mrn] + 1
            df2.at[4,'methodName'] = methodName_aux_4
            df2.at[4,'Total methods'] =len(methodName_aux_4)

        if sum(mrs) == 5:
            methodName_aux_5.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[5, mrn] = df2.at[5, mrn] + 1
            df2.at[5,'methodName'] = methodName_aux_5
            df2.at[5,'Total methods'] =len(methodName_aux_5)

        if sum(mrs) == 6:
            methodName_aux_6.append(row.at['Method Name'])
            indices = [index for index, element in enumerate(mrs) if element == 1]
            for i in indices:
                mrn = mrs_name[i]
                df2.at[6, mrn] = df2.at[6, mrn] + 1
            df2.at[6,'methodName'] = methodName_aux_6
            df2.at[6,'Total methods'] =len(methodName_aux_6)

    for index, row in df2.iterrows():
        add = row.at['ADD']
        mul = row.at['MUL']
        per = row.at['PER']
        inc = row.at['INC']
        exc = row.at['EXC']
        inv = row.at['INV']

        mrs = [add, mul, per, inc, exc, inv]
        
        df2.at[index, 'Total_MRs'] = sum(mrs)
    
    #print(df2)
    df2.to_csv('MRsFrec-gruped.csv')
    



if __name__ == '__main__':
    import click

    @click.command()
    @click.option('-i', '--file', 'input', help='Path file')

    def main(input):

        df = pd.read_csv(input)

        def_plot(df)
        #counter_MRs(df)



main()