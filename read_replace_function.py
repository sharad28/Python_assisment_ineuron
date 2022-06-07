class replace_s:
    def replace_string(self,path,original,update):
        #for reading data
        try:
            with open(path,'r') as f:
                data = f.read()
                self.data = data.replace(original,update)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        #for writing data on same file
        try:
            with open(path,w) as f:
                f.write(self.data)
        except Exception as e:
            print("error occur while writing on file")



