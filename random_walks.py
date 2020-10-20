import matplotlib.pyplot as plt
import math
import numpy as np
import random
import pylab

def plotEfficiency (navigationalEfficiencies): # Plot: Nagivational Efficiency/Time Step
    # Plot: Efficiency (Navigation)

    # Weight: W = 0
    plt.xlabel('time step')
    plt.ylabel('navigational efficiency')
    plt.plot(navigationalEfficiencies[0], label = "Theta = Pi/24")
    plt.plot(navigationalEfficiencies[1], label= "Theta = Pi/12")
    plt.plot(navigationalEfficiencies[2], label="Theta = Pi/3")
    plt.title ("Mean Navigational Efficiency versus Time Steps (W = 0)")
    plt.legend(loc='best', prop={'size': 10})
    plt.show() # Graph: Display

    # Weight: W = 0.5
    plt.xlabel('time step')
    plt.ylabel('navigational efficiency')
    plt.plot(navigationalEfficiencies[3], label= "Theta = Pi/24")
    plt.plot(navigationalEfficiencies[4], label= "Theta = Pi/12")
    plt.plot(navigationalEfficiencies[5], label= "Theta = Pi/3")
    plt.title ("Mean Navigational Efficiency versus Time Steps (W = 0.5)")
    plt.legend(loc='best', prop={'size': 10})
    plt.show() # Graph: Display

    # Weight: W = 1
    plt.xlabel('time step')
    plt.ylabel('navigational efficiency')
    plt.plot(navigationalEfficiencies[6], label= "Theta = Pi/24")
    plt.plot(navigationalEfficiencies[7], label= "Theta = Pi/12")
    plt.plot(navigationalEfficiencies[8], label= "Theta = Pi/3")
    plt.title ("Mean Navigational Efficiency versus Time Steps (W = 1)")
    plt.legend(loc='best', prop={'size': 10})
    plt.show() # Graph: Display

def weightEfficiency (efficiencies, weights):
    maximumEfficiency = max(efficiencies) # Record: Maximum: Efficienies (Navigational)
    print ("Navigation Efficiency (Maximum): ", maximumEfficiency, efficiencies.index(maximumEfficiency))
    return efficiencies.index(maximumEfficiency)

nagivationalEfficienciesVar = [] # List: Nagivational Efficiences (Paramter: Variations)

class Random_Walks_Python():
    def random_walks(self):
        N = 500 #no of steps per trajectory
        realizations = 50 #number of trajectories (Directions)
        v = 1.0 #velocity (step size)
        theta_s_array = [round(math.pi/24,4),round(math.pi/12,4),round(math.pi/3,4)] #the width of the random walk turning angle distribution (the lower it is, the more straight the trajectory will be)

        # Array: Weight: (Original)
        w_array = [0.0, 0.5, 1.0] # w is the weighting given to the directional bias (and hence (1-w) is the weighting given to correlated motion)

        # Weights: Navigational Efficiency (Maximum)
        # w_array = np.linspace(0,1,100) # [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6 ,0.7, 0.8, 0.9, 1.0]

        # Efficiency (Navigational) (Final)
        efficiencyFinal = []

        # print("Weight: Array: ", w_array)

        ratio_theta_s_brw_crw = 1
        plot_walks = 1
        count = 0

        directionThetaX = 0
        directionThetaY = 0
        efficiency_array = np.zeros([len(theta_s_array),len(w_array)])

        # print (round (0.6666, 0))
        # for w_i in range(0, 10): # For: All W
        for w_i in range(len(w_array)): # For: All W
            w = w_array[w_i]
            print("w: ", w)
            for theta_s_i in range(len(theta_s_array)): # For: All Theta
                theta_s_crw = np.multiply(ratio_theta_s_brw_crw,theta_s_array[theta_s_i])
                theta_s_brw = theta_s_array[theta_s_i]

                # Theta: Navigational Efficiency (Maximum) CRW: Pi/30, BRW: Pi/3
                # theta_s_crw = math.pi/30
                # theta_s_brw = math.pi/3

                x,y = self.BRCW(N,realizations, v, theta_s_crw,theta_s_brw,w)
                for i in range (N):
                    directionThetaX = x[:,i]
                    directionThetaY = y[:,i]
                    # print(directionThetaX)
                    # [] Rows: Directions (50) Columns: Time Steps (500)
                # directionThetaY = directionThetaY + y
                print ("Theta: ", theta_s_array[theta_s_i])

                if plot_walks == 1:
                    count += 1
                    # plt.figure(count)
                    # plt.plot(x.T, y.T)
                    # plt.axis('equal')
                print ("Navigational Efficiency: ", np.divide(np.mean(x[:,-1]-x[:,0]),(v*N)))
                # print ("Weight: ", w_i, "Theta: ", theta_s_i)
                efficiencyFinal.append(np.divide(np.mean(x[:,-1]-x[:,0]),(v*N)))
                efficiency_array[theta_s_i, w_i] = np.divide(np.mean(x[:,-1]-x[:,0]),(v*N)) # Iterate: 0, n - 1
                # print ("Nagivational Efficiency: ", efficiency_array[-1])
                # print (efficiency_array)
                efficiencies = [] # Efficiencies (List)
                steps = [] # Steps (List)

                # print ("Weight: ", w_array [w_i], "Theta: ", theta_s_array[theta_s_i], "Efficiency: ", efficiency_array)

                for i in range (0, N - 1): # For: 0 - (N - 1)
                    efficiencies.append (np.divide(np.mean(x[:,i]-x[:,0]),(v*i))) # Mean: Efficiency (Navigational)
                    steps.append (i) # Time: Step

                # print (x[:,-1]-x[:, i])
                # print ("Efficiency (Navigational) Final: ", efficiencyFinal)
                nagivationalEfficienciesVar.append(efficiencies)
                # print (len(nagivationalEfficienciesVar))
                print(" ")

            # print ("Weight: ", w_i, "Theta: ", theta_s_i, "Efficiency: ", efficiency_array)
            # print (efficienc)

        legend_array = []
        w_array_i = np.repeat(w_array,len(efficiency_array))
        for theta_s_i in range(0, len(theta_s_array)):
            legend_array.append(["$\theta^{*CRW}=$", (ratio_theta_s_brw_crw*theta_s_array[theta_s_i]),"$\theta^{*BRW}=$",(theta_s_array[theta_s_i])])

        # Plot: Nagivational Efficiencies
        plotEfficiency (nagivationalEfficienciesVar)

        # Calculate: Maximum: Efficiency (Navigational)
        # weightElement = round((weightEfficiency (efficiencyFinal, w_array))/3, 0)
        # print ("Navigation Efficiency (Maximum) Weight: ", w_array[weightElement])

        # print ("Weight Element: ", weightElement)

#The funciton generate 2D Biased Corrolated Random Walks
    def BRCW(self,N, realizations, v, theta_s_crw, theta_s_brw,w): # Random Walk
        X = np.zeros([realizations, N]) #
        Y = np.zeros([realizations, N])
        theta = np.zeros([realizations, N])
        X[:, 0] = 0
        Y[:, 0] = 0
        theta[:, 0] = 0

        for realization_i in range(realizations):
            for step_i in range(1,N):
                theta_crw = theta[realization_i][step_i-1]+(theta_s_crw* 2.0 * (np.random.rand(1,1)-0.5))
                theta_brw = (theta_s_brw* 2.0 * (np.random.rand(1,1)-0.5))

                X[realization_i, step_i] = X[realization_i][step_i-1] + (v * (w*math.cos(theta_brw))) + ((1-w) * math.cos(theta_crw))
                Y[realization_i, step_i] = Y[realization_i][step_i-1] + (v* (w*math.sin(theta_brw))) +((1-w)* math.sin(theta_crw))

                current_x_disp = X[realization_i][step_i] - X[realization_i][step_i-1]
                current_y_disp = Y[realization_i][step_i] - Y[realization_i][step_i-1]
                current_direction = math.atan2(current_y_disp,current_x_disp)

                theta[realization_i, step_i] = current_direction

        return X, Y

rdm_plt = Random_Walks_Python()
rdm_plt.random_walks()
