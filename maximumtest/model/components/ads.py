from selene import command
from selene.support.conditions import have
from selene.support.shared import browser

ads = browser.elements('.popmechanic-js-animation-wrapper')


def remove(*, amount, timeout):
    if ads.with_(timeout=timeout).wait.until(have.size_greater_than_or_equal(amount)):
        ads.perform(command.js.remove)
