from sklearn import tree
features = [[400, "2"], [350, "2"], [80, "9"], [150, "8"]]
labels = ["Car", "Car", "MiniVan", "MiniVan"]
x = input("Speed: ") #for user input 
y = input("Seats:" ) #for user input
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[x, y]]))