"use strict";
////////////////////////////////////////////////////////////////////////////////
// 🛑 Nothing in here has anything to do with Remix, it's just a fake database
////////////////////////////////////////////////////////////////////////////////
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.deleteContact = exports.updateContact = exports.getContact = exports.createEmptyContact = exports.getContacts = void 0;
const match_sorter_1 = require("match-sorter");
// @ts-expect-error - no types, but it's a tiny function
const sort_by_1 = __importDefault(require("sort-by"));
const tiny_invariant_1 = __importDefault(require("tiny-invariant"));
////////////////////////////////////////////////////////////////////////////////
// This is just a fake DB table. In a real app you'd be talking to a real db or
// fetching from an existing API.
const fakeContacts = {
    records: {},
    getAll() {
        return __awaiter(this, void 0, void 0, function* () {
            return Object.keys(fakeContacts.records)
                .map((key) => fakeContacts.records[key])
                .sort((0, sort_by_1.default)("-createdAt", "last"));
        });
    },
    get(id) {
        return __awaiter(this, void 0, void 0, function* () {
            return fakeContacts.records[id] || null;
        });
    },
    create(values) {
        return __awaiter(this, void 0, void 0, function* () {
            const id = values.id || Math.random().toString(36).substring(2, 9);
            const createdAt = new Date().toISOString();
            const newContact = Object.assign({ id, createdAt }, values);
            fakeContacts.records[id] = newContact;
            return newContact;
        });
    },
    set(id, values) {
        return __awaiter(this, void 0, void 0, function* () {
            const contact = yield fakeContacts.get(id);
            (0, tiny_invariant_1.default)(contact, `No contact found for ${id}`);
            const updatedContact = Object.assign(Object.assign({}, contact), values);
            fakeContacts.records[id] = updatedContact;
            return updatedContact;
        });
    },
    destroy(id) {
        delete fakeContacts.records[id];
        return null;
    },
};
////////////////////////////////////////////////////////////////////////////////
// Handful of helper functions to be called from route loaders and actions
function getContacts(query) {
    return __awaiter(this, void 0, void 0, function* () {
        yield new Promise((resolve) => setTimeout(resolve, 500));
        let contacts = yield fakeContacts.getAll();
        if (query) {
            contacts = (0, match_sorter_1.matchSorter)(contacts, query, {
                keys: ["first", "last"],
            });
        }
        return contacts.sort((0, sort_by_1.default)("last", "createdAt"));
    });
}
exports.getContacts = getContacts;
function createEmptyContact() {
    return __awaiter(this, void 0, void 0, function* () {
        const contact = yield fakeContacts.create({});
        return contact;
    });
}
exports.createEmptyContact = createEmptyContact;
function getContact(id) {
    return __awaiter(this, void 0, void 0, function* () {
        return fakeContacts.get(id);
    });
}
exports.getContact = getContact;
function updateContact(id, updates) {
    return __awaiter(this, void 0, void 0, function* () {
        const contact = yield fakeContacts.get(id);
        if (!contact) {
            throw new Error(`No contact found for ${id}`);
        }
        yield fakeContacts.set(id, Object.assign(Object.assign({}, contact), updates));
        return contact;
    });
}
exports.updateContact = updateContact;
function deleteContact(id) {
    return __awaiter(this, void 0, void 0, function* () {
        fakeContacts.destroy(id);
    });
}
exports.deleteContact = deleteContact;
[
    {
        avatar: "https://sessionize.com/image/124e-400o400o2-wHVdAuNaxi8KJrgtN3ZKci.jpg",
        first: "Shruti",
        last: "Kapoor",
        twitter: "@shrutikapoor08",
    },
    {
        avatar: "https://sessionize.com/image/1940-400o400o2-Enh9dnYmrLYhJSTTPSw3MH.jpg",
        first: "Glenn",
        last: "Reyes",
        twitter: "@glnnrys",
    },
    {
        avatar: "https://sessionize.com/image/9273-400o400o2-3tyrUE3HjsCHJLU5aUJCja.jpg",
        first: "Ryan",
        last: "Florence",
    },
    {
        avatar: "https://sessionize.com/image/d14d-400o400o2-pyB229HyFPCnUcZhHf3kWS.png",
        first: "Oscar",
        last: "Newman",
        twitter: "@__oscarnewman",
    },
    {
        avatar: "https://sessionize.com/image/fd45-400o400o2-fw91uCdGU9hFP334dnyVCr.jpg",
        first: "Michael",
        last: "Jackson",
    },
    {
        avatar: "https://sessionize.com/image/b07e-400o400o2-KgNRF3S9sD5ZR4UsG7hG4g.jpg",
        first: "Christopher",
        last: "Chedeau",
        twitter: "@Vjeux",
    },
    {
        avatar: "https://sessionize.com/image/262f-400o400o2-UBPQueK3fayaCmsyUc1Ljf.jpg",
        first: "Cameron",
        last: "Matheson",
        twitter: "@cmatheson",
    },
    {
        avatar: "https://sessionize.com/image/820b-400o400o2-Ja1KDrBAu5NzYTPLSC3GW8.jpg",
        first: "Brooks",
        last: "Lybrand",
        twitter: "@BrooksLybrand",
    },
    {
        avatar: "https://sessionize.com/image/df38-400o400o2-JwbChVUj6V7DwZMc9vJEHc.jpg",
        first: "Alex",
        last: "Anderson",
        twitter: "@ralex1993",
    },
    {
        avatar: "https://sessionize.com/image/5578-400o400o2-BMT43t5kd2U1XstaNnM6Ax.jpg",
        first: "Kent C.",
        last: "Dodds",
        twitter: "@kentcdodds",
    },
    {
        avatar: "https://sessionize.com/image/c9d5-400o400o2-Sri5qnQmscaJXVB8m3VBgf.jpg",
        first: "Nevi",
        last: "Shah",
        twitter: "@nevikashah",
    },
    {
        avatar: "https://sessionize.com/image/2694-400o400o2-MYYTsnszbLKTzyqJV17w2q.png",
        first: "Andrew",
        last: "Petersen",
    },
    {
        avatar: "https://sessionize.com/image/907a-400o400o2-9TM2CCmvrw6ttmJiTw4Lz8.jpg",
        first: "Scott",
        last: "Smerchek",
        twitter: "@smerchek",
    },
    {
        avatar: "https://sessionize.com/image/08be-400o400o2-WtYGFFR1ZUJHL9tKyVBNPV.jpg",
        first: "Giovanni",
        last: "Benussi",
        twitter: "@giovannibenussi",
    },
    {
        avatar: "https://sessionize.com/image/f814-400o400o2-n2ua5nM9qwZA2hiGdr1T7N.jpg",
        first: "Igor",
        last: "Minar",
        twitter: "@IgorMinar",
    },
    {
        avatar: "https://sessionize.com/image/fb82-400o400o2-LbvwhTVMrYLDdN3z4iEFMp.jpeg",
        first: "Brandon",
        last: "Kish",
    },
    {
        avatar: "https://sessionize.com/image/fcda-400o400o2-XiYRtKK5Dvng5AeyC8PiUA.png",
        first: "Arisa",
        last: "Fukuzaki",
        twitter: "@arisa_dev",
    },
    {
        avatar: "https://sessionize.com/image/c8c3-400o400o2-PR5UsgApAVEADZRixV4H8e.jpeg",
        first: "Alexandra",
        last: "Spalato",
        twitter: "@alexadark",
    },
    {
        avatar: "https://sessionize.com/image/7594-400o400o2-hWtdCjbdFdLgE2vEXBJtyo.jpg",
        first: "Cat",
        last: "Johnson",
    },
    {
        avatar: "https://sessionize.com/image/5636-400o400o2-TWgi8vELMFoB3hB9uPw62d.jpg",
        first: "Ashley",
        last: "Narcisse",
        twitter: "@_darkfadr",
    },
    {
        avatar: "https://sessionize.com/image/6aeb-400o400o2-Q5tAiuzKGgzSje9ZsK3Yu5.JPG",
        first: "Edmund",
        last: "Hung",
        twitter: "@_edmundhung",
    },
    {
        avatar: "https://sessionize.com/image/30f1-400o400o2-wJBdJ6sFayjKmJycYKoHSe.jpg",
        first: "Clifford",
        last: "Fajardo",
        twitter: "@cliffordfajard0",
    },
    {
        avatar: "https://sessionize.com/image/6faa-400o400o2-amseBRDkdg7wSK5tjsFDiG.jpg",
        first: "Erick",
        last: "Tamayo",
        twitter: "@ericktamayo",
    },
    {
        avatar: "https://sessionize.com/image/feba-400o400o2-R4GE7eqegJNFf3cQ567obs.jpg",
        first: "Paul",
        last: "Bratslavsky",
        twitter: "@codingthirty",
    },
    {
        avatar: "https://sessionize.com/image/c315-400o400o2-spjM5A6VVfVNnQsuwvX3DY.jpg",
        first: "Pedro",
        last: "Cattori",
        twitter: "@pcattori",
    },
    {
        avatar: "https://sessionize.com/image/eec1-400o400o2-HkvWKLFqecmFxLwqR9KMRw.jpg",
        first: "Andre",
        last: "Landgraf",
        twitter: "@AndreLandgraf94",
    },
    {
        avatar: "https://sessionize.com/image/c73a-400o400o2-4MTaTq6ftC15hqwtqUJmTC.jpg",
        first: "Monica",
        last: "Powell",
        twitter: "@indigitalcolor",
    },
    {
        avatar: "https://sessionize.com/image/cef7-400o400o2-KBZUydbjfkfGACQmjbHEvX.jpeg",
        first: "Brian",
        last: "Lee",
        twitter: "@brian_dlee",
    },
    {
        avatar: "https://sessionize.com/image/f83b-400o400o2-Pyw3chmeHMxGsNoj3nQmWU.jpg",
        first: "Sean",
        last: "McQuaid",
        twitter: "@SeanMcQuaidCode",
    },
    {
        avatar: "https://sessionize.com/image/a9fc-400o400o2-JHBnWZRoxp7QX74Hdac7AZ.jpg",
        first: "Shane",
        last: "Walker",
        twitter: "@swalker326",
    },
    {
        avatar: "https://sessionize.com/image/6644-400o400o2-aHnGHb5Pdu3D32MbfrnQbj.jpg",
        first: "Jon",
        last: "Jensen",
        twitter: "@jenseng",
    },
].forEach((contact) => {
    fakeContacts.create(Object.assign(Object.assign({}, contact), { id: `${contact.first.toLowerCase()}-${contact.last.toLocaleLowerCase()}` }));
});
//# sourceMappingURL=data.js.map