# Minimum Viable Product

### The Problem:
Question/need:
There are a great many films made outside of the US from established centers such as Bollywood and Pinewood Studios, to resent entries like China and Nollywood. Most foreign produced films have a tough time breaking the U.S. box office, though recent successes like Crouching Tiger, Hidden Dragon and Amelie demonstrate an appetite for foreign films among American film-goers.

Is there a means to predict the success of a foreign film in the states? Can an accurate prediction model be created to assist film distributers when selecting a foreign film

### Selecting the data?
The list of foreign films from Box Office Mojo was used. It contains non-English language films distributed in the US since 1980. We considered use of a non-English language as the main language for the script as the criterion for a foreign film, because other factors, such as filming location or production company, make little sense in the globalized film industry and it means that all films share a similar characteristic that can impede success in the US market.

### Assumptions
We assumed that there were two main drivers behind the success of a foreign film in the US: (1) 'critical buzz', and (2) the number of awards a film had garnered. We used the _IMDB metascore_, an average of critical scores to measure 'critical buzz' and the number of award nominations. We measured success, our dependent variable, as the box office gross over the lifetime of the film, which was taken from Box Office Mojo.

### The Initial Results
The initial results show that these two factors do not predict the box office gross of a foreign film. The two scatterplots below show that awards and 'critical buzz' have at most a small positive effect on the gross, but it is most likely caused by a number of extreme examples that draw the line upwards.
#### Gross and Critical Buzz ('Metascore')
#### R-squared:
![Gross~Buzz](https://github.com/John-Keating/02-project_luther/blob/master/MVP_metascore.png)
#### Gross and Awards ('nominations')
#### R-squared:
![Gross~Awards](https://github.com/John-Keating/02-project_luther/blob/master/MVP_awards.png)

### Conclusions
It's a good thing that you called in the data scientists: the initial, and indeed, reasonable assumptions about predicting the success of a foreign film turn out not to be the case. It may be that this is an unpredictable market. One that you should avoid because of the inherent risks.

However, it may be that our research has gone down the wrong path and it is time to reasses.

The initial tack of the research project was far too elitist in its assumptions. What the critics and the industry choose to praise through awards and glowing reviews have little effect on what people go to watch. Rather than look at a top down approach, exploring what type of films, what languages in particular, succeed. Are low-budget, critically-ignored foriegn films a good bet? If so, can we predict it by looking at genre and language? Let's see. 
