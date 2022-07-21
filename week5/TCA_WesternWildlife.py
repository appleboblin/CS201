animals = [
    {
        "name": "Mule deer",
        "info": "The mule deer (Odocoileus hemionus) is a deer indigenous to western North America; it is named for its ears, which are large like those of the mule. Two subspecies of mule deer are grouped into the black-tailed deer.",
        "genus": "Odocoileus",
        "order": "Artiodactyla",
    },
    {
        "name": "White-tailed antelope squirrel",
        "info": "The white-tailed antelope squirrel (Ammospermophilus leucurus) is a diurnal species of ground squirrel, scientifically classified in the order Rodentia and family Sciuridae, found in arid regions of the southwestern United States and the Baja California Peninsula of northwestern Mexico.",
        "genus": "Ammospermophilus",
        "order": "Rodentia",
    },
    {
        "name": "Cougar",
        "info": "The cougar (Puma concolor) is a large cat native to the Americas. Its range spans from the Canadian Yukon to the southern Andes in South America and is the most widespread of any large wild terrestrial mammal in the Western Hemisphere. It is an adaptable, generalist species, occurring in most American habitat types. Due to its wide range, it has many names, including puma, mountain lion, catamount and panther.",
        "genus": "Puma",
        "order": "Carnivora",
    },
    {
        "name": "Coyote",
        "info": "The coyote (Canis latrans) is a species of canine native to North America. It is smaller than its close relative, the wolf, and slightly smaller than the closely related eastern wolf and red wolf. It fills much of the same ecological niche as the golden jackal does in Eurasia. The coyote is larger and more predatory and was once referred to as the American jackal by a behavioral ecologist. Other historical names for the species include the prairie wolf and the brush wolf.",
        "genus": "Canis",
        "order": "Carnivora",
    },
    {
        "name": "American badger",
        "info": "The American badger (Taxidea taxus) is a North American badger similar in appearance to the European badger, although not closely related. It is found in the western, central, and northeastern United States, northern Mexico, and south-central Canada to certain areas of southwestern British Columbia.",
        "genus": "Taxidea",
        "order": "Carnivora",
    },
    {
        "name": "Sea otter",
        "info": "The sea otter (Enhydra lutris) is a marine mammal native to the coasts of the northern and eastern North Pacific Ocean. Adult sea otters typically weigh between 14 and 45 kg (30 and 100 lb), making them the heaviest members of the weasel family, but among the smallest marine mammals. Unlike most marine mammals, the sea otter's primary form of insulation is an exceptionally thick coat of fur, the densest in the animal kingdom. Although it can walk on land, the sea otter is capable of living exclusively in the ocean.",
        "genus": "Enhydra",
        "order": "Carnivora",
    },
    {
        "name": "Steller sea lion",
        "info": "The Steller sea lion (Eumetopias jubatus), also known as the Steller's sea lion and northern sea lion, is a near-threatened species of sea lion in the northern Pacific. It is the sole member of the genus Eumetopias and the largest of the eared seals (Otariidae). Among pinnipeds, it is inferior in size only to the walrus and the two species of elephant seals. The species is named for the naturalist Georg Wilhelm Steller, who first described them in 1741. The Steller sea lion has attracted considerable attention in recent decades, owing to significant and largely unexplained declines in their numbers over an extensive portion of their northern range in Alaska.",
        "genus": "Eumetopias",
        "order": "Carnivora",
    },
    {
        "name": "Red fox",
        "info": 'The red fox (Vulpes vulpes) is the largest of the true foxes and one of the most widely distributed members of the order Carnivora, being present across the entire Northern Hemisphere including most of North America, Europe and Asia, plus parts of North Africa. It is listed as least concern by the IUCN. Its range has increased alongside human expansion, having been introduced to Australia, where it is considered harmful to native mammals and bird populations. Due to its presence in Australia, it is included on the list of the "world\'s 100 worst invasive species".',
        "genus": "Vulpes",
        "order": "Carnivora",
    },
    {
        "name": "Raccoon",
        "info": "The raccoon (/rəˈkuːn/ or US: /ræˈkuːn/, Procyon lotor), sometimes called the common raccoon to distinguish it from other species, is a mammal native to North America. It is the largest of the procyonid family, having a body length of 40 to 70 cm (16 to 28 in), and a body weight of 5 to 26 kg (11 to 57 lb). Its grayish coat mostly consists of dense underfur, which insulates it against cold weather. Three of the raccoon's most distinctive features are its extremely dexterous front paws, its facial mask, and its ringed tail, which are themes in the mythologies of the indigenous peoples of the Americas relating to the animal. The raccoon is noted for its intelligence, as studies show that it is able to remember the solution to tasks for at least three years. It is usually nocturnal and omnivorous, eating about 40% invertebrates, 33% plants, and 27% vertebrates.",
        "genus": "Procyon",
        "order": "Carnivora",
    },
    {
        "name": "Spotted skunk",
        "info": "The genus Spilogale includes all skunks commonly known as spotted skunks. Currently, there are four accepted extant species: S. gracilis, S. putorius, S. pygmaea, and S. angustifrons. New research, however, proposes that there may be up to seven",
        "genus": "Spilogale",
        "order": "Carnivora",
    }
]
def search(option, key):
    return next((i for i, item in enumerate(animals) if item[option] == key), None)
  
def get_animal_info(animal):
    try:
        return str(animals[search("name", animal)].get("info", ""))
    except:
        return ""
    
def get_animal_genus(animal):
    try:
        return str(animals[search("name", animal)].get("genus", ""))
    except:
        return ""

def get_animal_order(animal):
    try:
        return str(animals[search("name", animal)].get("order", ""))
    except:
        return ""

def lookup_by_order(order):
    try:
        output = []
        for animal in animals:
            orders = animal.get("order", "")
            if orders == order:
                output.append(animal.get("name"))
        output.sort()
        return output
    except:
        return ""
      
def export_all_animals():
    return animals
