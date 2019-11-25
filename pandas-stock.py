from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

amd = pd.read_csv("AMD.csv")
amd['Date'] = pd.to_datetime(amd.Date)

intel = pd.read_csv("INTC.csv")
intel['Date'] = pd.to_datetime(intel.Date)

nvidia = pd.read_csv("NVDA.csv")
nvidia['Date'] = pd.to_datetime(nvidia.Date)


amd_mean = amd["Close"].mean()
intel_mean = intel["Close"].mean()
nvidia_mean = nvidia["Close"].mean()


plt.figure("Tech Stock")
plt.plot(amd["Date"], amd["Close"], 'r-', linewidth=0.6, label="AMD Stock price, mean=" + str(amd_mean))
plt.plot(intel["Date"], intel["Close"], 'b-', linewidth=0.6, label="INTEL Stock price, mean=" + str(intel_mean))
# plt.plot(nvidia["Date"], nvidia["Close"], 'g-', linewidth=0.6, label="NVIDIA Stock price, mean=" + str(nvidia_mean))

plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
