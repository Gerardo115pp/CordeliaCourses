
const cordelia_server = CORDELIA_API;

function attributesToJson() {
    const json_data = {};
    console.log("AttributestoJson:" + this);
    Object.entries(this).forEach(([key, value]) => {
        if (!(this[key] instanceof Function) && key[0] !== '_') {
            json_data[key] = value;
        }
    });
    return JSON.stringify(json_data);
}

export class LoginRequest {
    constructor() {
        this.email = "";
        this.password = "";
    }

    toJson = attributesToJson.bind(this);

    do = callback => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        console.log("LoginRequest: " + this.toJson());

        const request = new Request(`${cordelia_server}/customers/customer/auth`, {method: 'POST', headers: headers, body: this.toJson()});
        
        fetch(request)
            .then(response => response.json())
            .then(data => {
                return callback(data);
            });
    }
}

export class SignUpRequest {
    constructor() {
        this.name = "";
        this.last_name = "";
        this.email = "";
        this.password = "";
    }

    toJson = attributesToJson.bind(this);

    do = callback => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');

        const request = new Request(`${cordelia_server}/customers/customer`, {method: 'POST', headers: headers, body: this.toJson()});

        fetch(request)
            .then(response => callback(response.status)); // if successful, return status code 201 and no body
    }
}

export class PasswordRecoveryRequest {
    constructor() {
        this.email = "";
    }

    toJson = attributesToJson.bind(this);

    do = () => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
    }
}