import matplotlib.pyplot as plt



def genSizes(contribution,gains,total):
	return [(contribution/total), (gains/total), ((total-contribution-gains)/total)]


def genPieChart(sizes, username):
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'Original Contribution', 'Staking Gains', 'Rest of Pool'
	explode = (0.04, 0.08, 0.0)  # "explode" the contribution and gains
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	#plt.show()
	plt.savefig(str(username)+".png")
