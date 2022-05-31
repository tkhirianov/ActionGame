# ActionGame
Educational project for the eng.speaking MIPT group in 2022 year.

This game will be the draft of the game with Battle Field for Actors.
Each type of actor will behave itself different way.

There are several heroes in the Battle Field.
Each hero is represented as a `class` in file `actor_***.py` where `***` is the name of the hero.
Classes of actors should be successors of the abstract base class Actor from `actor.py`.

To add hero into the game you need not only to create a class, but also modify `fabric.py` to call the construction of your objects.
