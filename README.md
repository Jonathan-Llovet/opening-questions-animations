# Opening Questions - Manim

## About
Code for videos on the [Opening Questions](https://www.youtube.com/channel/UCRQ5gGxixCkYamF5S3sU1hA) Youtube channel.

Opening Questions is here to make resources for people to learn and engage with computer science, programming, math and science (and how they have developed throughout history), and philosophy.

Projects with source code will have links to their own repositories.

Animations can be found in [opening-questions-manim/opening\_questions](https://github.com/Jonathan-Llovet/opening-questions-manim/tree/master/opening_questions)

The animations are made with the manim math animation engine, which was originally made by Grant Sanderson for 3b1b. Many thanks to Grant for creating this powerful tool, sharing it with the world, and making videos that help us see what's wonderful about math.

- [3b1b/manim on Github](https://github.com/3b1b/manim)
- [3b1b on Youtube](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)
- [www.3blue1brown.com](https://www.3blue1brown.com/)

I have included extensions of manim provided by the community in my scenes:

Thanks to Alexander Vázquez (Elteoremadebeethoven) for being so helpful with learning manim and supporting the community.
- [Elteoremadebeethoven on Github](https://github.com/Elteoremadebeethoven)
- [Theory of Beethoven on Youtube (English)](https://www.youtube.com/channel/UCxiWCEdx7aY88bSEUgLOC6A)

## Usage
I recommend using docker-compose to run manim. This simplifies the otherwise difficult installation process, and it helps prevent potential conflicts between dependencies here and other applications on your workstation.

---

### Install Docker
If it is not already installed, you'll need to [install Docker](https://docs.docker.com/get-docker/).

---

### Create .env for Environment Variables
Following this, create a file `.env` in the root of the project (i.e., `manim/.env`).
- This will contain environment variables for your manim container.

```shell
cd manim
touch .env
```

In `.env`, specify the `INPUT_PATH` that contains the Scenes that you want to render.

Then specify the `OUTPUT_PATH` that will be the output directory for artifacts created by manim.

```
INPUT_PATH=/Users/me/manim/
OUTPUT_PATH=/Users/me/manim/outputAnimations/
```

The `INPUT_PATH` and `OUTPUT_PATH` environment variables that you specified in `.env` are used to create volumes between your host machine and the docker image, which will allow docker to read and write files to and from your host machine in the mapped directories.
    - See [this page](https://docs.docker.com/storage/volumes/) for more information about volumes in docker.

---

### Building a Manim Docker Image
Following this, inside the `manim` directory, run the following:
```shell
docker-compose build
```

This will generate a docker image that you can render your scenes in.

---

### Running Manim
Finally, you can render your scenes in manim. Try one of the example scenes or one from opening_questions:

WarpSquare Scene:
```shell
docker-compose run manim example_scenes.py WarpSquare -l
```

Custom Example Scene:
```shell
docker-compose run manim opening_questions/learning_manim/learning_manim_001.py Shape -l
```

Syntax: 
```
docker-compose run manim <relative_path_to_scene>.py <classname> [flags]
```


## Resources
### Resources for Learning Manim
- Elteoremadebeethoven
    - [Manim Tutorial Youtube Series](https://www.youtube.com/watch?v=ENMyFGmq5OA&list=PL2B6OzTsMUrwo4hA3BBfS7ZR34K361Z8F)
    - [Animations With Manim](https://github.com/Elteoremadebeethoven/AnimationsWithManim)
- EulerTour
    - [EulerTour v2 - Web Based Version of Manim](https://eulertour.com/docs)
    - [Euler Tour, a web based sandbox for manim](https://eulertour.com/lab/example_scenes)
- malhotra5
    - [Manim-Tutorial](https://github.com/malhotra5/Manim-Tutorial)
    - [Manim-Guide](https://github.com/malhotra5/Manim-Guide)
- [Guided Tour from Talking Physics](https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/)
- [Manim Documentation](https://manim.readthedocs.io/en/latest/index.html) (In Progress - Please contribute!)
- [Reddit/r/manim/](https://www.reddit.com/r/manim/)

### Community
- [Manim Discord](https://discord.gg/mMRrZQW)

### Related Projects
- [eulerv2 - Web based frontend to manim](https://github.com/eulertour/eulerv2)
- [Manim.js - Manim in JavaScript](https://github.com/JazonJiao/Manim.js)
- [Primer - Animations with Blobs](https://github.com/Helpsypoo/primer)
- [krassowski/jupyter-manim](https://github.com/krassowski/jupyter-manim)
- [Vivek Verma](https://github.com/vivek3141)
    - [vcubingx on Youtube](https://www.youtube.com/channel/UCv0nF8zWevEsSVcmz6mlw6A)
- [Aathish Sivasubrahmanian](https://gitlab.com/aathish04/manim-projects/-/tree/master/)
    - [In Awe of Atoms](https://gitlab.com/aathish04/manim-projects/-/blob/master/In%20Awe%20of%20Atoms/AtomThroughAges.py)
- [TheRookieNerd/ManimMiniProjects](https://github.com/TheRookieNerd/ManimMiniProjects)
    - [The Rookie Nerds on Youtube](https://www.youtube.com/channel/UC88BHsvZyAbyBLjSoF_-OCA)
- [patrickshox/Ferrers-Diagrams](https://github.com/patrickshox/Ferrers-Diagrams)

### Other Animation Tools
- [Unity](https://unity.com/)
- [Blender](https://www.blender.org/)
