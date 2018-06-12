def moving_average():
    flag = True
    counter = 0
    data_sum =0
    moving_avg = 0
    while(flag):
        input_data = int(input("Enter the next number"))
        counter +=1
        data_sum +=input_data
        moving_avg = data_sum/counter
        print("moving average = {}".format(moving_avg))
        flag = int(input("Do you wanna enter more data? Enter 1 for True 0 for False"))
        if(flag != 1):
            break

moving_average()