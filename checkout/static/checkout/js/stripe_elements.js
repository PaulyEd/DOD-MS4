var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    var errorBtn = document.getElementById('submit-button');
    if (event.error) {
        var htmlError = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        var btnError = `
               <span class="icon">
               <i class="fas fa-exclamation-triangle"></i>
               </span><span class="font-weight-bold">Error</span>
        `
        $(errorDiv).html(htmlError);
        $(errorBtn).html(btnError);
        $(errorBtn).addClass("btn-danger disabled");
    } else {
        errorDiv.textContent = '';
        var btnSuccess = `
               <span class="font-weight-bold">Complete Order</span>
               <span class="icon">
               <i class="fas fa-lock"></i>
               </span>
        `
        $(errorBtn).html(btnSuccess);
        $(errorBtn).removeClass("btn-danger disabled");
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var htmlError = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>
        `;
            $(errorDiv).html(htmlError);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});