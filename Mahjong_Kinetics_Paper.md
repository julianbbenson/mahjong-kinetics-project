# The Law of the Wall: A Biochemical Analysis of Riichi Mahjong

**An Exploratory Winter Project** **Author:** Julian Benson  
**Dataset:** [Tenhou.net](https://tenhou.net/) 鳳凰卓 logs ($N = 1,087,446$)

![Real Mahjong Autotable Session](https://upload.wikimedia.org/wikipedia/commons/5/5c/Riichi_Mahjong_real_autotable_session.jpg)  
*(A live Riichi Mahjong session. Beneath the plastic tiles and the gambling, a rigid biochemical system is at work).*

---

## Pre-Prologue: The Anatomy of a Hand (A Primer)

Before we can discuss the physical chemistry of the game, we need to understand the biological structure of a Mahjong hand. 

Riichi Mahjong is a Japanese tile game played with three main suits (Characters, Circles, and Bamboo) numbered 1 through 9, plus Honor tiles (Winds and Dragons). Going forward, we will refer to these suits by their standard Japanese terms: **Man** (Characters), **Pin** (Circles), and **Sou** (Bamboo).

![Full Set of Japanese Mahjong Tiles](https://upload.wikimedia.org/wikipedia/commons/e/e0/Japanese_Mahjong_Tiles_1.jpg)  
*(A full layout of physical Mahjong tiles, including the standard suits, honors, and variant tiles like the Red Dora and Seasons).*

The objective is to draw and discard tiles until you complete a **14-tile hand**, perfectly structured into four sets of three (either sequences or triplets) and one pair. 

To build this hand, players draw from a central pool of face-down tiles called the **Wall**. While a full physical set contains 136 tiles, after the initial hands are dealt and the "dead wall" (a locked 14-tile reserve) is set aside, the active game begins with a "Live Wall" of exactly **70 tiles**. In biochemical terms, this live wall is your entire pool of available substrate. With every turn, four players draw from this pool, steadily depleting the environment's resources.

*A standard 14-tile winning hand:* ![Standard 14-tile winning hand](https://files.catbox.moe/xhc1kl.png)

When you are exactly one tile away from completing this structure, your hand is in a state called **Tenpai** (Ready). 

The incomplete part of your hand is called the **Wait** (Machi). In biochemical terms, this wait is your enzyme's "active site." The shape of this wait dictates how easily your hand can grab its final tile from the board. 

* **The Ryanmen Wait (Two-Sided):** You hold a 3 and a 4 of Pin. You are waiting for a 2 or a 5 to complete the sequence. This is a highly flexible, high-affinity active site because it accepts two different substrates.  
![Ryanmen wait](https://files.catbox.moe/6itrnz.png)

* **The Kanchan Wait (Closed):** You hold a 4 and a 6 of Man. You need exactly the 5 to fill the hole. This is a medium-affinity site.  
![Kanchan wait](https://files.catbox.moe/bqkkqq.png)

* **The Penchan Wait (Edge):** You hold a 1 and a 2 of Sou. You can only wait for a 3. Because it's locked to the absolute edge of the suit, it's a highly specific, low-affinity site.  
![Penchan wait](https://files.catbox.moe/noq4xm.png)

*(Note: In-line Mahjong tile diagrams sourced from [riichi.wiki](https://riichi.wiki))*

Keep these structures in mind. They are the enzymes we are about to test.

---

## Prologue: The Illusion of the Linear

We like to think of card and tile games as simple math. You have a deck, you have a wall. If there are 34 tiles left, and 2 of them are your winning tile, you have a certain percentage chance of drawing it. If the wall halves, your chances roughly halve. It's a linear, predictable, and frankly, boring way to view probability. 

For decades, Mahjong players have calculated "Uke-ire" (tile acceptance) based on this assumption. You count the tiles, you divide by the wall, you get a number.

**But wait.**

What if that fundamental assumption is entirely, catastrophically wrong? What if a Mahjong hand isn't a static mathematical equation, but a living, breathing, biological machine? What if, instead of statistics, we should be using physical chemistry?

This project started with a weird 3 AM thought: *When I call Riichi, my hand feels like an enzyme locking into place.* I decided to prove it. I harvested over a million high-level game logs from the Tenhou Houou (Phoenix) Room. And what I found may have shattered the linear probability model. Mahjong, it turns out, is strictly governed by the laws of stoichiometric biochemistry. 

Welcome to the Law of the Wall.

---

## Part 1: Evolutionary Divergence and the Exponential Payoff

To truly understand why the *Riichi* mechanic exists, we have to look at the game's phylogenetic tree.

Mahjong originated in China during the Qing dynasty, but it did not remain a monolith. Much like a rapidly mutating virus introduced to a vast new environment, the game spread across the provinces and immediately began splintering into dozens of localized, highly distinct regional variants. It underwent rapid Darwinian evolution. Sichuan rules stripped out the honor tiles entirely; Taiwanese rules expanded the hand size from 14 to 16. 

Just looking at the phylogenetic map of Mahjong variants within China alone is staggering:

![Map of Mahjong Variants in China](https://sloperama.com/pix/mjfaq23pic.png)  
*(The sheer density of regional mutation. And this is before the game ever crossed the ocean).*

If your grandma plays Mahjong alongside Bridge or Pinochle on a Tuesday afternoon, she is likely playing a variant of Hong Kong or traditional Chinese Mahjong. Despite the regional differences, these classic forms share a common genetic trait: they are highly social, additive games. You build a hand, you count up your points based on what you collected, and you win. It is a linear, low-energy metabolic cycle.

But in the 1920s, the game jumped the pond to Japan. And in the gambling parlors of the post-WWII Shōwa era, the game underwent a violent, high-stakes mutation: the introduction of the *Riichi* declaration. 

![Movie](https://files.catbox.moe/az8kz3.jpg)  
*(Mahjong Hōrōki (1984), set in the 1950s, is a stark, black-and-white dive into the gritty world of underground gambling in post-war Japan.)*

The Japanese variant shifted the scoring system from additive to **exponential**. 
In Riichi Mahjong, your score is calculated using two variables:
1. **Fu (Base Points):** The raw, structural difficulty of the tiles in your hand (e.g., holding edge tiles or triplets gives you more *fu*). 
2. **Han (Doubles):** Multipliers awarded for the rarity and beauty of the hand's pattern. 

The formula for calculating a hand's basic point payout is literally an exponential function:
$$Score \propto Fu \times 2^{Han+2}$$

Every time you add a *Han*, your score doubles. And here is the kicker: **Declaring Riichi adds a Han.** By announcing to the table that you are one tile away, and betting 1,000 points, you inject an exponential multiplier into your hand. 

![Mahjong Fu Scoring Table](https://i.redd.it/qf4ouub1oqra1.png)  
*(...and you thought Poker was hard enough! You can learn more about counting fu [here](https://majandofu.com/en-mahjong-fu-points)).*

### The Thermodynamic Analogy
If Chinese Mahjong is a simple, linear metabolic pathway, Riichi Mahjong is a highly regulated, exothermic explosion. 

In thermodynamics, reactions require an **Activation Energy ($E_a$)** to proceed. The 1,000-point bet required to declare Riichi is that activation energy. You invest energy to trigger the declaration because it acts as an **allosteric activator** for your score. By successfully completing the reaction, that single *Han* multiplier doubles your payout, resulting in a massive thermodynamic release of points. 

But you cannot get that exponential payout without paying a biological price: the loss of flexibility.

---

## Part 2: The Protein Dynamics of a Mahjong Hand

This brings us to the physical structure of the tiles. 

When you are building a hand, your 13 tiles form a sequence. In structural biology, proteins aren't just rigid clumps; they undergo **conformational breathing**. They wiggle, they shift, they open and close. 

![Protein Conformational Change](https://upload.wikimedia.org/wikipedia/commons/7/72/ChimeraX_rendering_of_myoglobin_%28PDB_2SPL%29.png)  
*(A standard protein structure, demonstrating how amino acid sequences fold into active shapes).*

When you have an open, "Damaten" (silent) hand in Mahjong, your hand is breathing. You draw a 4-Pin, you drop a 1-Pin—the structure of your hand physically shifts its active site. You might smoothly mutate a rigid, low-affinity *Penchan* wait into a highly flexible *Ryanmen* wait to accommodate whatever tile is most abundant in your environment. You are flexible. 

But then, you decide you want that exponential payout. You declare **Riichi**. 

You pay your activation energy. You rotate your discard. And suddenly, your hand is frozen. You are no longer allowed to change its shape. In biochemistry, this is called a **Conformational Lock**. You have frozen your enzyme into a highly specific state designed to catch exactly one type of substrate: your winning tile. 

The question is: *When* is the optimal time to lock that conformation? If you lock it too early, you might miss out on a better shape. But if you lock it too late... well, that's where the math gets terrifying.

---

## Part 3: The Ghosts of Kinetics Past

Before we look at the data, we need to talk about the architects of this mathematical model. 

If you're going to model enzyme dynamics, you use the Michaelis-Menten equation. But who actually were they?

Leonor Michaelis was a German biochemist in the early 1900s. Brilliant guy. But the real star of the show, the one who doesn't get enough real estate on your Biology textbooks, was **Maud Menten**. Menten was an absolute force of nature. At a time when women were largely barred from scientific research, she crossed the ocean to work with Michaelis in Berlin. She was a polymath—she mastered half a dozen languages, painted exhibition-worthy art, played the clarinet, and co-authored the most famous equation in biological kinetics in 1913. 

![Maud Menten](https://scientiablog.com/wp-content/uploads/2018/12/fascinante-kxhg-u601670279925szg-624x385la-verdad.jpg)  

They realized that chemical reactions don't just happen at a flat rate. They are *substrate-limited*. If you have a ton of enzymes but only a few molecules of substrate (the stuff the enzyme acts on), the reaction crawls. If you flood the system with substrate, the enzymes work at maximum speed until they hit a physical bottleneck—their $V_{max}$. 

The equation they derived looks like this:

$$v = \frac{V_{max} [S]}{K_m + [S]}$$

* **$v$**: The reaction velocity. (For us: **Win Probability**)
* **$V_{max}$**: The absolute maximum speed if substrate was infinite.
* **$[S]$**: The concentration of the substrate. (For us: **Live tiles remaining in the Wall**)
* **$K_m$**: The Michaelis Constant. The exact substrate concentration where the reaction is functioning at exactly half of its maximum capacity. 

So, I took this 110-year-old equation designed for cellular metabolism, fed it 1,087,446 Mahjong games, and asked the computer: *Does the Wall behave like a chemical substrate?*

![Spock and Computer](https://i0.wp.com/www.geeksandbeats.com/wp-content/uploads/2016/01/Star-Trek-Memory.jpg?w=640&ssl=1)  
*(If you don't care about the Python code, just pretend I'm Spock leaning over a glowing console, asking the ship's computer to calculate the optimal binding affinity of a space-tile).*

---

## Part 4: The Discovery of $K_m = 64$

To test the hypothesis, I wrote a Python harvester to parse the JSON logs. I didn't want static end-of-game data; I needed to capture the exact thermodynamic moment a player decided to expend their activation energy.

Here is the core logic from `harvest_data.py`. When the script detects a 'reach' (Riichi declaration), it locks in the exact amount of "substrate" left in the wall. 

```python
# From harvest_data.py: The Conformational Lock detector
if evt_type == 'reach':
    actor = event.get('actor')
    riichi_players[actor] = {
        'concentration': wall_tiles, # [S]: How much substrate is left?
        'turn': current_turn         # When did the enzyme lock?
    }
    riichis_found += 1

# If the reaction successfully yields a product (a win), we log a 1.
if evt_type == 'hora':
    winner = event.get('actor')
    if winner in riichi_players:
        data = riichi_players[winner]
        writer.writerow([filename, data['turn'], data['concentration'], 1])
        del riichi_players[winner]

```

Once I had the raw kinetic data, I passed it through `analyze_kinetics.py`. This script relies on the `scipy.optimize` library to forcefully fit the experimental Mahjong data to the 110-year-old equation Menten and Michaelis wrote.

```python
# From analyze_kinetics.py: The Spectrophotometer
def michaelis_menten(S, Vmax, Km):
    return (Vmax * S) / (Km + S)

# S_data = Tile Concentration, V_data = Win Rates
# We ask SciPy to find the theoretical limits of the Mahjong Wall
popt, pcov = curve_fit(michaelis_menten, S_data, V_data, p0=[0.6, 20])
Vmax_fit, Km_fit = popt

```

When I plotted the output, it wasn't a straight line. It was a textbook hyperbolic saturation curve ($R^2 > 0.98$).

![Experimental Saturation Curve](https://files.catbox.moe/kh0a0c.png)
*(The final kinetics curve calculated from the Tenhou logs).*

**The Constants:**

* **$V_{max} = 1.38$**: This means if the Mahjong wall were infinite, the theoretical maximum win rate approaches a constant limit dictated by the game's structural constraints.
* **$K_m = 63.9$ Tiles**: *This is the holy grail.* The system reaches half-maximum efficiency when there are exactly ~64 tiles left in the wall.

### 64: What's In A Number?

Before we talk about the game mechanics, can we just pause and appreciate the sheer metaphysical weight of the number 64? It is a number that seems almost hardcoded into the fabric of the universe.

In structural biology, there are exactly 64 codons in the human genetic code that dictate how our DNA is translated into proteins. In game theory, there are 64 squares on a chessboard, the ultimate grid of perfect information. In computer science, Base64 is a foundational data encoding scheme. Even the ancient Chinese philosophers obsessed over it—there are exactly 64 hexagrams in the *I Ching* (the Book of Changes), which feels profoundly appropriate for a game born from Chinese tile sets. It’s as if this specific integer is the universe's preferred container for complex, systemic information.

![I Ching Mandala](https://www.adamapollo.com/wp-content/uploads/2019/11/knowledge-iching-mandala.jpg)  
*(Too esoteric?)*

Anyway, sorry for the tangent. Back to the tiles.

Think about the rules of Mahjong. How many tiles are in the live wall when the game begins?
**70 tiles.**

Do you see the problem?

If a biological system has a $K_m$ of 64, it means it *needs* at least 64 units of substrate just to function at 50% efficiency. To reach peak efficiency, it needs hundreds of units.

But a Mahjong game *starts* with only 70 tiles.

This means that from the very first draw, **Mahjong is played in a state of catastrophic substrate starvation.** The "enzyme" never even gets close to operating at maximum capacity. We are living at the extreme, highly sensitive bottom-left corner of the Michaelis-Menten curve.

---

## Part 5: The Strategic Paradigm Shift (The Rule of 64)

Because we operate in this starvation zone, the drop-off in win probability is brutal and non-linear.

With 4 players drawing tiles, the wall depletes at 4 tiles per turn.

* **Turn 1:** 66 tiles left. (We are barely above $K_m$).
* **Turn 6:** 46 tiles left. (We have fallen drastically below $K_m$).
* **Turn 12:** 22 tiles left. (Kinetic failure).

**The Myth of the "Late Riichi"**  
Players often delay calling Riichi to try and improve their wait—hoping to mutate a bad *Penchan* into a glorious, multi-sided *Ryanmen*. But the kinetics prove this is almost always a mathematical blunder.

Once you cross Turn 6, the substrate concentration ($[S]$) drops so far below the $K_m$ that your reaction velocity collapses. You can have the best, most beautiful 3-sided wait in the world, but if you lock that conformation on Turn 12, *the physical chemistry of the board cannot support the reaction.* There isn't enough substrate left colliding with your hand to drive the reaction to a product (a win).

**Our Verdict:** The math dictates that early Riichi (Turns 1-5) is the only time the enzyme operates efficiently. If you are past Turn 8, your enzyme is dead. Fold the hand.

### But wait... The Wald's Ghost Objection

If you are a veteran player, you're likely currently screaming at your monitor. "Julian, this is catastrophic. This implies the game is over by Turn 8! I’ve won on Turn 14 with a bad wait hundreds of times. My own experience contradicts your so-called 'Kinetic Failure'!"

It’s a fair point. If the win rate is so abysmal past Turn 8, why does anyone still bother playing? Is the model broken? Did we chase a hyperbolic ghost?

Actually, what we’ve chanced upon here is another manifestation of **The Survivorship Bias of the Midgame**, or what I call **Wald’s Kinetic Ghost**.

![Wald](https://files.catbox.moe/lnl92p.webp)  
*(Aren't I great with names? Just imagine ol' Wald above glowing and floating. I'd thought of a Casper joke but forgot it...)*

During WWII, the statistician Abraham Wald looked at returning bombers covered in bullet holes. The military wanted to armor the areas with the most holes. Wald said no—armor the places with *no* holes, because the planes hit in those spots never made it back to be counted.

![Survivorship Bias Plane](https://www.amicus.co.nz/wp-content/uploads/2024/07/plane.png)  
*(The most-reposted, least-understood diagram on the Internet.)*

When you win on Turn 14, you are seeing the "plane that returned." You are looking at a successful reaction that occurred against all physical odds. What our Michaelis-Menten model captures is the **aggregate graveyard**. For every one player who wins a "Late Riichi" on Turn 14, our million-game dataset shows thousands of "enzymes" that locked their conformation, failed to find a substrate, and were essentially "denatured" by a faster player or an exhausted wall.

We suffer from an anecdotal delusion. Because we remember the high-payout, late-game wins, we assume the "velocity" of the game is still high. But the biochemistry doesn't lie. By the time you hit Turn 12, you aren't playing Mahjong anymore; you are a struggling protein in a frozen solution, praying for a stray substrate molecule (winning tile) that has likely already been consumed by your neighbors.

You are a ghost in the mahjong machine, living on the tail of a curve that has already hit zero.

---

## Intermission: A Moment of Decompression

We’ve traveled a long way from a stray 3 AM thought about protein folding. We’ve waded through the ghosts of WWII statisticians, the metaphysical weight of ancient Chinese hexagrams, and the cold, unyielding curve of substrate starvation. It’s easy to get lost in the "heavy" tone of the math—to see Mahjong as a solved, cynical machine where your fate is decided by Turn 8.

But if this project has proven anything, it’s that a single, curious question can lead you down some incredibly strange alleyways. This project ended up being much more than just winning a tile game; through it, we've realized that the same laws governing the microscopic dance of life in your cells are reflected in the clatter of plastic tiles on a tabletop.

If you’re new to Mahjong, don't let the "Rule of 64" scare you off. The math describes the boundaries of the cage, but the fun is in how you navigate it. Go play a game. Get on [Tenhou](https://tenhou.net/4/), install the [English UI extension](https://chromewebstore.google.com/detail/tenhou-english-ui/jdackjfahmdepglkioclfdhbhdplnana?pli=1), feel the "conformational breathing" of your own hand, and see if you can beat the kinetics. 

![Gameplay](https://i.imgur.com/HnnCpYb.jpeg) 
*Sometimes, the best way to understand a system is to simply become a part of the reaction.*

![Manga Panel](https://i.snap.as/DsSaiEOz.jpg)  
*(Ignore the sourpuss above. Seriously, go for it!)*

---

## Part 6: The Horizon (Bioinformatics x Game Theory)

If treating a Mahjong hand as an enzyme works this perfectly, it blows the doors wide open for other applications of computational biology in imperfect information games. What else could we do?

**1. Treating Discard Pools as Biological Pathways (Reactome Analysis)**
In bioinformatics, we use pathway analysis to map how biological networks interact. What if we map game trees not as static chess-like nodes, but as biological pathways? A player's discard history is basically a metabolic pathway. If they discard a 1-Pin, then a 2-Pin, then a 9-Sou, that sequence is a "metabolite cascade." We could use visual pathway analysis to predict exactly what "downstream product" (winning hand) they are trying to synthesize.



**2. Allosteric Inhibition (The Math of Folding)**
When an opponent calls Riichi, how do you defend? In biochemistry, an inhibitor binds to an enzyme to stop it from working. Your defensive discards are basically **competitive inhibitors**. Could we calculate the $K_i$ (inhibitor constant) of certain safety tiles? Can we mathematically prove which discards lower the opponent's reaction velocity the fastest?

**3. The Darwinian Meta: Evolutionary Game Strategy**
We could treat the various "Meta-strategies" of Mahjong (like the shift from *Menzen* play to *Naki* speed play) as a literal population of organisms competing for resources. We could apply the **Price Equation** from evolutionary biology to track how "strategic traits" are passed down or discarded based on their fitness (payout). Could a mutation in a single player’s discarding habit eventually lead to a "Speciation Event" where an entire server tier evolves a completely different kinetic profile? We are talking about the emergence of a self-correcting, artificial ecosystem of logic.

The wall is not random chance but a living, breathing organism—and we're just beginning to sequence its genome!

---
*Data compiled from 2025 Tenhou logs. Analyzed using Python and Scipy.*