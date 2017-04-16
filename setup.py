import cx_Freeze

executables = [cx_Freeze.Executable("sg.py")]
cx_Freeze.setup( name="Slither"
                 options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","image.png"]}},
                 description = "Slither game ",
                 executables = executables
                 )
                 
