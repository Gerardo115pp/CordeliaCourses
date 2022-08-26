
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

    do = (callback, on_error) => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        console.log("LoginRequest: " + this.toJson());

        const request = new Request(`${cordelia_server}/customers/customer/auth`, {method: 'POST', headers: headers, body: this.toJson()});
        
        fetch(request)
            .then(response => {
                if (response.status >= 200 && response.status < 300) {
                    return response.json().then(data => callback(data));
                } else {
                    on_error(response.status);
                }
            })
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

export class ChangePasswordRequest {
    constructor() {
        this._token = "";
        this.new_password = "";
    }

    toJson = attributesToJson.bind(this);

    do = (on_success, on_error) => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', `Bearer ${this._token}`);

        const request = new Request(`${cordelia_server}/customers/customer/password`, {method: 'PATCH', headers: headers, body: this.toJson()});
    
        fetch(request)
            .then(response => {

                if (response.status >= 200 && response.status < 300) {
                    on_success(response);
                } else {
                    on_error(response.status);
                }
            })
    }
}

export class PasswordRecoveryRequest {
    constructor() {
        this.email = "";
    }

    toJson = attributesToJson.bind(this);

    do = (on_success, on_error) => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        
        const request = new Request(`${cordelia_server}/password-recovery`, {method: 'POST', headers: headers, body: this.toJson()});
        fetch(request)
            .then(response => {
                if (response.status >= 200 && response.status < 300) {
                    return on_success(response);
                } else {
                    on_error(response.status);
                }
            })
    }
}
export class GetCustomerCoursesRequest {
    constructor() {
        this.token = ""
    }

    toJson = attributesToJson.bind(this);

    do = callback => {
        if (this.token === "") {
            return;
        }

        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', `Bearer ${this.token}`);

        const request = new Request(`${cordelia_server}/courses/`, {method: 'GET', headers: headers});
        fetch(request)
            .then(response => response.json())
            .then(data => {
                return callback(data);
            });
    }
}

export class GetCourseRequest {

    constructor(token, id) {
        this.token = token;
        this.id = id;
    }

    toJson = attributesToJson.bind(this);

    do = callback => {
        if (this.token === undefined || this.id === undefined) {
            return;
        }

        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', `Bearer ${this.token}`);

        const request = new Request(`${cordelia_server}/courses/course?id=${this.id}`, {method: 'GET', headers: headers});
        fetch(request)
            .then(response => response.json())
            .then(data => {
                return callback(data);
            });
    }
}

export class GetDataVersion {
    toJson = attributesToJson.bind(this);

    do = callback => {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');

        const request = new Request(`${cordelia_server}/data-version`, {method: 'GET', headers: headers});
        fetch(request)
            .then(response => response.json())
            .then(data => {
                return callback(data);
            });
    }
}