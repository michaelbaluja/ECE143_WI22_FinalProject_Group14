import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def why_high_rating():
    '''This function draws plenty of pictures that shows why some recipes' ratings are high.

    -------

    '''
    recipes = pd.read_csv('RAW_recipes.csv')
    interactions = pd.read_csv('RAW_interactions.csv')
    
    rating = interactions[['recipe_id','rating']]
    time = recipes[['id','minutes']]
    steps = recipes[['id','n_steps']]
    nutrition = recipes[['id','nutrition']]
    n_ingredients = recipes[['id','n_ingredients']]
    description = recipes[['id','description']]
    tags = recipes[['id','tags']]
    review = interactions[['rating','review']]
    
    rating5id = rating.loc[rating.rating == 5]
    rating4id = rating.loc[rating.rating == 4]
    rating3id = rating.loc[rating.rating == 3]
    rating2id = rating.loc[rating.rating == 2]
    rating1id = rating.loc[rating.rating == 1]
    
    t5_time = []
    for i in rating5id['recipe_id']:
        t5_time.append(time[time.id == i]['minutes'].item())
    t4_time = []
    for i in rating4id['recipe_id']:
        t4_time.append(time[time.id == i]['minutes'].item())
    t3_time = []
    for i in rating3id['recipe_id']:
        t3_time.append(time[time.id == i]['minutes'].item())
    t2_time = []
    for i in rating2id['recipe_id']:
        t2_time.append(time[time.id == i]['minutes'].item())
    t1_time = []
    for i in rating1id['recipe_id']:
        t1_time.append(time[time.id == i]['minutes'].item())
    
    s5_steps = []
    for i in rating5id['recipe_id']:
        s5_steps.append(steps[steps.id == i]['n_steps'].item())
    s4_steps = []
    for i in rating4id['recipe_id']:
        s4_steps.append(steps[steps.id == i]['n_steps'].item())
    s3_steps = []
    for i in rating3id['recipe_id']:
        s3_steps.append(steps[steps.id == i]['n_steps'].item())
    s2_steps = []
    for i in rating2id['recipe_id']:
        s2_steps.append(steps[steps.id == i]['n_steps'].item())
    s1_steps = []
    for i in rating1id['recipe_id']:
        s1_steps.append(steps[steps.id == i]['n_steps'].item())
    
    rating5steps = s5_steps
    rating4steps = s4_steps
    rating3steps = s3_steps
    rating2steps = s2_steps
    rating1steps = s1_steps
    
    rating5time = t5_time
    rating4time = t4_time
    rating3time = t3_time
    rating2time = t2_time
    rating1time = t1_time
    
    for i in range(910):
        rating5steps.pop(rating5time.index(max(rating5time)))
        rating5time.pop(rating5time.index(max(rating5time)))
    for i in range(500):
        rating4steps.pop(rating4time.index(max(rating4time)))
        rating4time.pop(rating4time.index(max(rating4time)))
    for i in range(200):
        rating3steps.pop(rating3time.index(max(rating3time)))
        rating3time.pop(rating3time.index(max(rating3time)))
    for i in range(200):
        rating2steps.pop(rating2time.index(max(rating2time)))
        rating2time.pop(rating2time.index(max(rating2time)))
    for i in range(300):
        rating1steps.pop(rating1time.index(max(rating1time)))
        rating1time.pop(rating1time.index(max(rating1time)))
    
    for i in range(300):
        rating5steps.pop(rating5time.index(min(rating5time)))
        rating5time.pop(rating5time.index(min(rating5time)))
    for i in range(200):
        rating4steps.pop(rating4time.index(min(rating4time)))
        rating4time.pop(rating4time.index(min(rating4time)))
    for i in range(200):
        rating3steps.pop(rating3time.index(min(rating3time)))
        rating3time.pop(rating3time.index(min(rating3time)))
    for i in range(200):
        rating2steps.pop(rating2time.index(min(rating2time)))
        rating2time.pop(rating2time.index(min(rating2time)))
    for i in range(300):
        rating1steps.pop(rating1time.index(min(rating1time)))
        rating1time.pop(rating1time.index(min(rating1time)))
        
    Tmean5 = sum(rating5time)/len(rating5time)
    Tmean4 = sum(rating4time)/len(rating4time)
    Tmean3 = sum(rating3time)/len(rating3time)
    Tmean2 = sum(rating2time)/len(rating2time)
    Tmean1 = sum(rating1time)/len(rating1time)
    
    x = np.arange(5)+1
    Tmean = [Tmean1,Tmean2,Tmean3,Tmean4,Tmean5]
    plt.plot(x,Tmean, color='#00AA00', label='label1', linewidth=1.0)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Mean Cooking Time', fontsize=12)
    plt.grid('on')
    plt.show()
    
    Smean5 = sum(rating5steps)/len(rating5steps)
    Smean4 = sum(rating4steps)/len(rating4steps)
    Smean3 = sum(rating3steps)/len(rating3steps)
    Smean2 = sum(rating2steps)/len(rating2steps)
    Smean1 = sum(rating1steps)/len(rating1steps)
    
    Smean = [Smean1,Smean2,Smean3,Smean4,Smean5]
    plt.plot(x,Smean, color='#00AA00', label='label1', linewidth=1.0)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Mean Cooking Steps', fontsize=12)
    plt.grid('on')
    plt.show()
    
    coor5 = []
    coor4 = []
    coor3 = []
    coor2 = []
    coor1 = []
    for i in range(len(rating5time)):
        coor5.append([rating5time[i],rating5steps[i],5])
    for i in range(len(rating4time)):
        coor4.append([rating4time[i],rating4steps[i],4])
    for i in range(len(rating3time)):
        coor3.append([rating3time[i],rating3steps[i],3])
    for i in range(len(rating2time)):
        coor2.append([rating2time[i],rating2steps[i],2])
    for i in range(len(rating1time)):
        coor1.append([rating1time[i],rating1steps[i],1])
    
    
    from mpl_toolkits.mplot3d import Axes3D
    
    x5 = []
    y5 = []
    z5 = []
    for i in range(len(coor5)):
        x5.append(coor5[i][0])
        y5.append(coor5[i][1])
        z5.append(coor5[i][2])
    x4 = []
    y4 = []
    z4 = []
    for i in range(len(coor4)):
        x4.append(coor4[i][0])
        y4.append(coor4[i][1])
        z4.append(coor4[i][2])
    x3 = []
    y3 = []
    z3 = []
    for i in range(len(coor3)):
        x3.append(coor3[i][0])
        y3.append(coor3[i][1])
        z3.append(coor3[i][2])
    x2 = []
    y2 = []
    z2 = []
    for i in range(len(coor2)):
        x2.append(coor2[i][0])
        y2.append(coor2[i][1])
        z2.append(coor2[i][2])
    x1 = []
    y1 = []
    z1 = []
    for i in range(len(coor1)):
        x1.append(coor1[i][0])
        y1.append(coor1[i][1])
        z1.append(coor1[i][2])
        
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(y5,z5,x5, cmap='b') 
    ax.scatter3D(y4,z4,x4, cmap='b') 
    ax.scatter3D(y3,z3,x3, cmap='b') 
    ax.scatter3D(y2,z2,x2, cmap='b') 
    ax.scatter3D(y1,z1,x1, cmap='b')   
    plt.ylabel(u'rating', fontsize=12)
    plt.xlabel(u'steps', fontsize=12)
    
    plt.show()
    
    counter = 0
    for i in range(len(rating5time)):
        if(rating5time[i]>100):
            counter += 1
    percent5 = counter/len(rating5time)
    counter = 0
    for i in range(len(rating4time)):
        if(rating4time[i]>100):
            counter += 1
    percent4 = counter/len(rating4time)
    counter = 0
    for i in range(len(rating3time)):
        if(rating3time[i]>100):
            counter += 1
    percent3 = counter/len(rating3time)
    counter = 0
    for i in range(len(rating2time)):
        if(rating2time[i]>100):
            counter += 1
    percent2 = counter/len(rating2time)
    counter = 0
    for i in range(len(rating1time)):
        if(rating1time[i]>100):
            counter += 1
    percent1 = counter/len(rating1time)
    
    
    
    counter = 0
    for i in range(len(rating5time)):
        if(rating5steps[i]>20):
            counter += 1
    percent55 = counter/len(rating5time)
    counter = 0
    for i in range(len(rating4time)):
        if(rating4steps[i]>20):
            counter += 1
    percent44 = counter/len(rating4time)
    counter = 0
    for i in range(len(rating3time)):
        if(rating3steps[i]>20):
            counter += 1
    percent33 = counter/len(rating3time)
    counter = 0
    for i in range(len(rating2time)):
        if(rating2steps[i]>20):
            counter += 1
    percent22 = counter/len(rating2time)
    counter = 0
    for i in range(len(rating1time)):
        if(rating1steps[i]>20):
            counter += 1
    percent11 = counter/len(rating1time)
    
    x = np.arange(5)+1
    p = [percent1,percent2,percent3,percent4,percent5]
    plt.plot(x,p, color='#00AA00', label='label1', linewidth=1.0)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Percentage of time>100', fontsize=12)
    plt.show()
    
    pp = [percent11,percent22,percent33,percent44,percent55]
    plt.plot(x,pp, color='#00AA00', label='label1', linewidth=1.0)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Percentage of steps>20', fontsize=12)
    plt.show()
    
    time_temp = {'1':rating1time,'2':rating2time,'3':rating3time,'4':rating4time,'5':rating5time}
    time = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in time_temp.items()])) 
    time.boxplot()#这里，pandas自己有处理的过程，很方便哦。  
    plt.ylabel("time")  
    plt.xlabel("rating")#我们设置横纵坐标的标题。  
    plt.show()
    
    steps_temp = {'1':rating1steps,'2':rating2steps,'3':rating3steps,'4':rating4steps,'5':rating5steps}
    c = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in steps_temp.items()])) 
    c.boxplot()#这里，pandas自己有处理的过程，很方便哦。  
    plt.ylabel("steps")  
    plt.xlabel("rating")#我们设置横纵坐标的标题。  
    title = "Cooking Complexity vs Rating"
    plt.title(title)
    plt.grid('on')
    plt.show()
    
    
    
    grid = np.zeros((20,20))
    cnt = np.zeros((20,20))
    
    # coor1[:,0].max()
    coor1 = np.array(coor1)
    temp1 = (coor1[:,0]-1)//40
    temp2 = coor1[:,1]-1
    pos = (temp1<20) & (temp2<20)
    grid[temp1[pos],temp2[pos]] += 1
    cnt[temp1[pos],temp2[pos]] += 1
    
    coor2 = np.array(coor2)
    temp1 = (coor2[:,0]-1)//40
    temp2 = coor2[:,1]-1
    pos = (temp1<20) & (temp2<20)
    grid[temp1[pos],temp2[pos]] += 2
    cnt[temp1[pos],temp2[pos]] += 1
    
    coor3 = np.array(coor3)
    temp1 = (coor3[:,0]-1)//40
    temp2 = coor3[:,1]-1
    pos = (temp1<20) & (temp2<20)
    grid[temp1[pos],temp2[pos]] += 3
    cnt[temp1[pos],temp2[pos]] += 1
    
    coor4 = np.array(coor4)
    temp1 = (coor4[:,0]-1)//40
    temp2 = coor4[:,1]-1
    pos = (temp1<20) & (temp2<20)
    grid[temp1[pos],temp2[pos]] += 4
    cnt[temp1[pos],temp2[pos]] += 1
    
    coor5 = np.array(coor5)
    temp1 = (coor5[:,0]-1)//40
    temp2 = coor5[:,1]-1
    pos = (temp1<20) & (temp2<20)
    grid[temp1[pos],temp2[pos]] += 5
    cnt[temp1[pos],temp2[pos]] += 1
    
    zeros_pos = (cnt == 0)
    m = np.zeros((20,20))
    m[~zeros_pos]= grid[~zeros_pos]/cnt[~zeros_pos]
    
    plt.imshow(m, cmap='hot', interpolation='nearest')
    plt.ylabel("steps")  
    plt.xlabel("time")#我们设置横纵坐标的标题。 
    title = "Cooking Time,Steps heat map"
    plt.title(title)
    plt.show()
    
    
    return 0
    
    
    
