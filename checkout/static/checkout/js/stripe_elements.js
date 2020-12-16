var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
  base: {
    color: '#32325d',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    },
    ':-webkit-autofill': {
      color: '#32325d',
    },
  },
  invalid: {
    color: '#ff000',
    iconColor: '#ff000',
    ':-webkit-autofill': {
      color: '#ff000',
    },
  },
  complete: {
    color: '#5cb85c',
    iconColor: '#5cb85c',
    ':-webkit-autofill': {
      color: '#5cb85c',
    },
    '::placeholder': {
        color: '#5cb85c',
    },
  },
};
var card = elements.create('card', {style: style});
card.mount('#card-element');
