from rlEnv import RlEnv
import numpy as np

def main ():
    env = RlEnv()
    observations = env.reset()

    verbose = False

    for step in range(1000):
        action = np.random.choice(env._ActionSpace, p=np.array([0.9, 0.1])) # random policy

        if verbose:
            print("action: ", action)

        observations, reward, terminated, shouldQuit = env.step(action)

        if verbose:
            print("observations: ", observations)
            print("reward: ", reward)
            print("terminated: ", terminated)
            print("shouldQuit: ", shouldQuit)

        if shouldQuit:
            break

        if terminated:
            observations = env.reset()

    env.close()
    return 0


if __name__=="__main__":
    main()