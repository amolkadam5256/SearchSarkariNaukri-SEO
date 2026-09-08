# 12 — MARATHI CONTENT SPECIFICATION

**Section:** Marathi Language Content  
**Priority:** P2  
**Type:** Content Specification  
**Status:** Implementation Ready

---

## Marathi Content Strategy

### Language Support

The current page already has मराठी (Marathi) support. Improve it with:

1. Comprehensive Marathi content
2. Proper language markup
3. Language switch functionality
4. Correct hreflang if separate URL

---

## Marathi Content

### H2 in Marathi
```
महाराष्ट्र जिल्हानिहाय सरकारी नोकरी
```

### Introduction in Marathi
```
महाराष्ट्रातील जिल्हानिहाय सरकारी नोकरी शोधण्यासाठी आपण्याला या पृष्ठावर अपडू शकते. पुणे, मुंबई, नागपूर, नाशिक आणि इतर सर्व ३६ जिल्ह्यांमध्ये सरकारी भरती आणि शासकीय नोकऱ्यांची माहिती मिळेल आहे.

प्रत्येक जिल्ह्यासाठी अलग पृष्ठ आहे जिथे त्या जिल्ह्यातील सध्याच्या सरकारी नोकऱ्यांची माहिती मिळते. पात्रता, रिक्त्या, अर्ज करण्याची तारीख आणि अधिकृत जाहिरात या पृष्ठावर उपल्या जाहिरातीत असते.

सरकारी नोकऱ्यांसाठी पात्रता विभिन्न असते. काही भरतींसाठी १०वी पास असते तर काहींसाठी १२वी पास किंव पदवी असते. अधिकृत जाहिरातीत पात्रता तपासणे आवश्यक आहे.
```

### Key Information in Marathi

#### District Information
```
महाराष्ट्रात ३६ जिल्हे आहेत
६ प्रदेश आहेत
प्रत्येक जिल्ह्यासाठी अलग सरकारी नोकरी
```

#### Eligibility Information
```
पात्रता: १०वी पास, १२वी पास, पदवीधर, डिप्लोमा
वयोमर्यादा: भरतीनुसार वेगळी
आरक्षण: आरक्षित वर्गांसाठी वयोमर्यादा सूट
```

#### Application Process
```
अधिकृत जाहिरात वाचा
पात्रता तपासा
अर्ज करण्याची शेवटची तारीख तपासा
अधिकृत पोर्टलवर अर्ज करा
```

---

## Implementation

### HTML Language Attribute
```html
<section aria-labelledby="marathi-content" lang="mr">
  <h2 id="marathi-content">महाराष्ट्र जिल्हानिहाय सरकारी नोकरी</h2>
  <p>Marathi content here...</p>
</section>
```

### Language Switch (If Separate URL)
```html
<a href="/districts?lang=mr" hreflang="mr">मराठी</a>
<a href="/districts?lang=en" hreflang="en">English</a>
```

### Hreflang (If Separate URL)
```html
<link rel="alternate" hreflang="en" href="https://www.searchsarkarinaukri.com/districts">
<link rel="alternate" hreflang="mr" href="https://www.searchsarkarinaukri.com/districts?lang=mr">
```

---

## District Names in Marathi

| English | Marathi |
|---------|---------|
| Pune | पुणे |
| Mumbai City | मुंबई शहर |
| Mumbai Suburban | मुंबई उपनगर |
| Nagpur | नागपूर |
| Nashik | नाशिक |
| Solapur | सोलापूर |
| Latur | लातूर |
| Kolhapur | कोल्हापूर |
| Aurangabad (Chhatrapati Sambhajinagar) | छत्रपती संभाजीनगर |
| Amravati | अमरावती |
| Akola | अकोला |
| Jalgaon | जळगाव |
| Dhule | धुळे |
| Nanded | नांदेड |
| Satara | सातारा |
| Sangli | सांगली |
| Ratnagiri | रत्नागिरी |
| Sindhudurg | सिंधुदुर्ग |
| Raigad | रायगड |
| Thane | ठाणे |
| Palghar | पालघर |
| Beed | बीड |
| Jalna | जालना |
| Parbhani | परभणी |
| Hingoli | हिंगोली |
| Dharashiv | धाराशिव |
| Yavatmal | यवतमाळ |
| Buldhana | बुलढाणा |
| Washim | वाशिम |
| Wardha | वर्धा |
| Chandrapur | चंद्रपूर |
| Gadchiroli | गडचिरोली |
| Bhandara | भंडारा |
| Gondia | गोंदिया |
| Nandurbar | नंदुरबार |
| Ahilyanagar | अहिल्यानगर |

---

## Implementation Checklist

### Content
- [ ] Marathi H2 added
- [ ] Marathi introduction added
- [ ] Key information in Marathi
- [ ] District names in Marathi
- [ ] Accurate translations

### Technical
- [ ] lang="mr" attribute added
- [ ] Language switch implemented (if applicable)
- [ ] hreflang tags added (if separate URL)
- [ ] UTF-8 encoding ensured
- [ ] Font support for Devanagari script

### UX
- [ ] Language switch visible
- [ ] Clear indication of language
- [ ] Easy to switch between languages
- [ ] Consistent design across languages

---

**Last Updated:** 8 September 2026  
**Status:** Implementation Ready