import pandas as pd
import numpy as np
import logging
import sys

iserror=False
# def check_exception():
n=len(sys.argv)
if n!=2:
    iserror=True
    logging.error('give correct number of parameters>>> one parameter= file_name.csv')
    raise Exception("give correct number of parameter>>>> one parameter= file_name.csv ")
    logging.shutdown()
    # exit()
else:
    fl_name=sys.argv[1]
    tap=np.char.isnumeric(fl_name)
    if tap==True:
        iserror=True
        logging.error("Enter non integer filename")
        raise Exception("Enter non integer filename")
        logging.shutdown()
        # exit()
    else:
        try:
            db=pd.read_csv(fl_name)
            if len(db.columns)!=6:
                iserror=True
                logging.error("Only 6 columns are allowed in input file")
                raise Exception("Only 6 columns are allowed in input file")
                logging.shutdown()
                # exit()
            else:
                col1=db.columns
                col2=['RollNumber', 'P1', 'P2', 'P3', 'P4', 'P5']
                for i in range(len(col1)):
                    if col1[i]!=col2[i]:
                        iserror=True
                        logging.error("Columns name should be in 'RollNumber', 'P1', 'P2', 'P3', 'P4', 'P5' ")
                        raise Exception("Columns name should be in 'RollNumber', 'P1', 'P2', 'P3', 'P4', 'P5' ")
                        logging.shutdown()
                        # exit()
        except IOError:
            iserror=True
            logging.error('File not found')
            print("File not found ")
            # exit()
        logging.shutdown()
        

def unique(list1):
    list_set=set(list1)
    unique_list=list(list_set)
    return unique_list

def main():
    # logging.basicConfig(filename='101916056-1.log', level=logging.INFO)
    
    # check_exception()

    if iserror==False:
        # print("bas khatam 1")
        df = pd.read_csv(sys.argv[1])
       


if __name__ == '__main__':
    main()