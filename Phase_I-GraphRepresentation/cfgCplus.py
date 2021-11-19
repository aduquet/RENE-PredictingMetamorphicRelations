import subprocess
import glob as gl
# Pip upgrade

# subprocess.run('pip install --upgrade pip')

# Click library
#subprocess.run('pip install click')


if __name__ == '__main__':  
    import click

    @click.command()
    @click.option('-i', '--file', 'data', help='Path of labelled Dataset')

    def main(data):

        dot_path = gl.glob(data)

        for i in dot_path:

            a_mainPath_name = i.split('\\')[-1]
            mainPath_name = a_mainPath_name.split('.')[0]
            print(mainPath_name, a_mainPath_name)
            #a = 'clang -S -emit-llvm ' + '"' +i+'"' + ' -o ' + mainPath_name + '.dll'
            a = 'opt -dot-cfg ' + '"'+ i + '"'
            print(a)
            subprocess.run(a)
        #dot_path = gl.glob(dot_input)
        #clang -S -emit-llvm add_two_array_values.cpp -o diag.ll

main()