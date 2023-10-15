# Guess My Number: Flask

The goal is to practice with the basics of Flask: routes and templates.

## Features

- index page should tell the user about the game, and have a link to start the
    game, at the url `/game`
- When they click to start the game, the user should be shown a page with numbers
  to guess. Each number should link to the 'guess page' for that number, like
  `/guess/31` for 31.
- When they click a number, the app should tell them if the number was correct,
    too high, or too low, and show a link back to guess again

This is what the page of numbers to guess should look like:

![demo of number guess page](numbers-to-guess.png)

## Notes

- All the routes should use the HTTP GET method (no POST or other kinds of
requests for now)
- Don't be afraid to copy/paste code from index.html to your other template
    files as you get started

## Starter Code

There is an app.py file that renders the index.html template file.

You should write the other routes in app.py and create additional template files for
the other pages of the application.

Start the development app by running:

```sh
flask run
```

## Testing

You should run your app and check that behaves as expected by trying the game in
the browser.

You can also run the automated tests to check whether your solution matches the
expectation. Gradescope will use the automated tests to score your answer. Run
`pytest test_app.py` to test your app.

## Deployment

Use [https://render.com/](render) to deploy your app into the web. Add the deployed app into the submision url.

## Bonus

This is intended to be a simple project to make sure you know the basics of
routing and templates. If you have more time and want to experiment, you can
also:

- add a stylesheet and a favicon (refer to the material about serving static files)
- Offer a "hint" button that, when clicked, provides a clue. This could be a range in which the target number lies, or a vague statement about the number.
- Introduce levels of difficulty. As the user progresses, the range of numbers increases, or the hints become more vague.
- Allow only a certain number of guesses. If the user exceeds this limit, they have to restart the game.

If you complete the bonus tasks, you should still submit a version of the
project that works using links, not a form.
