from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

fsize = 10
tsize = 10
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
plt.rcParams["figure.figsize"] = (6, 5)
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

    ax = plt.figure
    ax = df.plot.bar(stacked=True, color=['#565656', '#720022'])
    ax.set_xticklabels(names)

    plt.xlabel("Metamorphic relations")
    plt.ylabel("Count")
    plt.legend(('Does apply','Does not apply'), fancybox=True, shadow=True, ncol=2,  bbox_to_anchor=(0.5, 1.05), loc='upper center')
    plt.savefig("Total number of methods that satisfies or non-satisfies each metamorphic relation.pdf")
    plt.show()

if __name__ == '__main__':
    import click

    @click.command()
    @click.option('-i', '--file', 'input', help='Path file')

    def main(input):

        df = pd.read_csv(input)

        def_plot(df)



main()