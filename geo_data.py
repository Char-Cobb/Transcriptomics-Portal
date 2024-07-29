import sys
import os, subprocess
import requests


class downloadNCBIFiles:
   
    #download files from NCBI
    def getGEOfiles(self, accs, root_path):
        accList = []
        accs = accs
        
        #Convert IDs to GSE, make ids into list - helper Function
        with open(accs, 'r') as f:
            for line in f:
                pre = line[:4]
                if pre == "2000":
                    gse = "GSE" + line[4:-1] #replace the first four digits(2000) with GSE, remove the last \n character
                    accList.append(gse)
                else:
                    gse = "GSE" + line[3:-1] #replace the first three digits(200) with GSE, remove the last \n character
                    #accList.append(gse)

        print(accList[0])
        root_path = root_path
        count = 0
        for i in accList:
            cmd = "mkdir " + root_path + "/{i}".format(i=i)
            print(cmd)
            subprocess.run(cmd, shell=True, check=True)

            #get RNA-seq raw counts matrix
            url = "https://www.ncbi.nlm.nih.gov/geo/download/?type=rnaseq_counts&acc={i}&format=file&file={i}_raw_counts_GRCh38.p13_NCBI.tsv.gz"
            get = requests.get(url.format(i=i), allow_redirects=True)
            if get.status_code == 200:
                with open('{root}/{i}/{i}_raw_counts_GRCh38.p13_NCBI.tsv.gz'.format(i=i, root=root_path), 'wb') as f:
                    f.write(get.content)
                    f.close()

            #get RNA-seq normalized counts matrix - FPKM
            url = "https://www.ncbi.nlm.nih.gov/geo/download/?type=rnaseq_counts&acc={i}&format=file&file={i}_norm_counts_FPKM_GRCh38.p13_NCBI.tsv.gz"
            get = requests.get(url.format(i=i), allow_redirects=True)
            if get.status_code == 200:
                with open('{root}/{i}/{i}_norm_counts_FPKM_GRCh38.p13_NCBI.tsv.gz'.format(i=i, root=root_path), 'wb') as f:
                    f.write(get.content)
                    f.close()

            #get RNA-seq normalized counts matrix - TPM
            url = "https://www.ncbi.nlm.nih.gov/geo/download/?type=rnaseq_counts&acc={i}&format=file&file={i}_norm_counts_TPM_GRCh38.p13_NCBI.tsv.gz"           
            get = requests.get(url.format(i=i), allow_redirects=True)
            if get.status_code == 200:
                with open('{root}/{i}/{i}_norm_counts_TPM_GRCh38.p13_NCBI.tsv.gz'.format(i=i, root=root_path), 'wb') as f:
                    f.write(get.content)
                    f.close()

            
        return("Job is done!")


if __name__ == '__main__':
    args = sys.argv
    if len(args)!=3:
        print("Wrong number of argunents passed to the script. Please try again using exact 2 arguments in the right order")
        exit()

    download = downloadNCBIFiles()
    download.getGEOfiles(args[1], args[2])


