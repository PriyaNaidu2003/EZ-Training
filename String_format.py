age=36
a=1
txt="{}. my age is {}"
print(txt.format(a,age))

name='Alex'
years=30
city='Ballari'
job='SWE'
color='Blue'
output="My name is {0}. I have been staying in {2} for last {1} years and I am a {3}. My favourite color is {4}."
print(output.format(name,years,city,job,color))

output="My name is {na}. I have been staying in {ci} for last {yr} years and I am a {jo}. My favourite color is {cl}."
print(output.format(na=name,yr=years,ci=city,jo=job,cl=color))

output="My name is {}. I have been staying in {} for last {} years and I am a {}. My favourite color is {}."
print(output.format(name,city,years,job,color))




n=6
pf=[2, 3]
a=[1,5,6,3,2,4]
num=6

