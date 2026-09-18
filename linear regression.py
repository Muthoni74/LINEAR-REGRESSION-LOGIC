xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [2.9, 3.4, 4.9, 4.7, 6.2, 6.9, 7.3, 8.6]
w, b = 0.0, 0.0 #width #bias
lr = 0.01 # learning rate decides how big each correction may be
for epoch in range(1000): #one full path through the data is called an epoch
  dw, db = 0.0, 0.0
  for x, y in zip(xs, ys):
    pred = w * x + b # for each point a line makes a guess + bias
    err =  pred - y # for each error guess- truth
    dw += 2 * err * x / len(xs)
    db += 2 * err / len(xs)
  w -= lr * dw # the line moves one full step
  b -= lr * db