# each item in the manifest is an item and its weight
manifest =[["bananas", 15], ["mattresses", 34], ["dog kennels", 42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]
cargo_weight = 0
cargo_hold = []
for cargo in manifest:
    print("debug: the weight is currently {}".format(cargo_weight))
    print("debug: if we add {}, weight will be {}".format(cargo[0], cargo_weight + cargo[1]))
    after_loading_cargo_weight = cargo_weight + cargo[1]
    if after_loading_cargo_weight >= 100:
        print("debug: breaking loop now!")
        break
    else:
        print("debug: adding item {}".format(cargo[0]))
        print("debug: with weight {}".format(cargo[1]))
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]


print(cargo_weight)
print(cargo_hold)
