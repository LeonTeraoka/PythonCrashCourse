scores = [91, 45, 74, 50, 37, 68, 84, 70]
a_list = []
a_list = []
b_list = []
c_list = []
d_list = []
for score in scores:
	if score >= 80:
		a_list.append(score)
	elif score >= 60:
		b_list.append(score)
	elif score >=40:
		c_list.append(score)
	else:
		d_list.append(score)
print("Aランクの個数 :", len(a_list))
print("Bランクの個数 :", len(b_list))
print("Cランクの個数 :", len(c_list))
print("Dランクの個数 :", len(d_list))
