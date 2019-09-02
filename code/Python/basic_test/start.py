from class_op import multiop

#new model method

def main():
    print("start") 
    mu_test=multiop()
    print("value add test {}".format(mu_test.add(3,5)))
    print("value div test {}".format(mu_test.div(3,5)))
    



if __name__=='__main__':main()