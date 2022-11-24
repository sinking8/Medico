# Medico

A Medical assistant which is developed with the motive of assisting users at any position.
Helps users by providing medical assistance.

<hr>

## Features

- Predicts the illness of the user.
- Takes account of all factors which plays a major role in a user’s health.
- If illness is critical and not curable using home remedies doctors of respective specializations are recommended.

<hr>

## Working

- The data which is the Medical History of the user as well as the current user symptoms are taken as input
- The collected data is preprocessed accordingly. Padding and removal of redundant records are removed
- The preprocessed data is feeded to the pre trained model.
- The Illness as well as the remedies are found out with the help of the output of the model. Then the predicted data is displayed to the user.

<hr>

## Future Enhancements

- Authenticity of user data could not be checked.
- Generalization of illness.
- Support for multiple languages needs to be attained
  in order to make medibot much more effective.

<hr>

## Screenshots

<img src="https://github.com/sinking8/MEDICO/blob/main/screenshots/1.PNG"/>

<hr>

### Quick Start

1. Clone the repo

```
$ git clone https://github.com/sinking8/Medico.git
$ cd Medico
```

2. Initialize and activate a virtualenv:

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

5. Run the development server:

```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)
