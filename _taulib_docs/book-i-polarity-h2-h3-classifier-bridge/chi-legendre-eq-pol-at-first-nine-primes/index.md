---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_legendre_eq_Pol_at_first_nine_primes",
  "permalink": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/chi-legendre-eq-pol-at-first-nine-primes/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H2H3ClassifierBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.H2H3ClassifierBridge::chi_legendre_eq_Pol_at_first_nine_primes",
  "declaration_slug": "chi-legendre-eq-pol-at-first-nine-primes",
  "kind": "theorem",
  "name": "chi_legendre_eq_Pol_at_first_nine_primes",
  "module_name": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/",
  "source_line_start": 136,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L136-L154",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H2H3ClassifierBridge",
        "url": "/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L136-L154",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Polarity.H2H3ClassifierBridge](/verify/taulib/docs/book-i-polarity-h2-h3-classifier-bridge/)
- Source path: [`TauLib/BookI/Polarity/H2H3ClassifierBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H2H3ClassifierBridge.lean#L136-L154)
- Source range: L136-L154
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The bundled Wave 17 ↔ Wave 18-19a bridge theorem**: at every
    one of the first 9 primes, the Wave 17 abstract `chi`
    instantiated with `legendreBClass` agrees with Wave 19a's
    concrete `Pol`.

    This packages the per-prime native_decide proofs above into a
    single conjunctive statement, the form most useful for
    downstream consumers wanting the bridge at the standard
    9-prime test range. -/
```

## Source Excerpt

```lean
theorem chi_legendre_eq_Pol_at_first_nine_primes :
    chi legendreBClass 2  = Pol 2  ∧
    chi legendreBClass 3  = Pol 3  ∧
    chi legendreBClass 5  = Pol 5  ∧
    chi legendreBClass 7  = Pol 7  ∧
    chi legendreBClass 11 = Pol 11 ∧
    chi legendreBClass 13 = Pol 13 ∧
    chi legendreBClass 17 = Pol 17 ∧
    chi legendreBClass 19 = Pol 19 ∧
    chi legendreBClass 23 = Pol 23 :=
  ⟨chi_legendre_eq_Pol_at_2,
   chi_legendre_eq_Pol_at_3,
   chi_legendre_eq_Pol_at_5,
   chi_legendre_eq_Pol_at_7,
   chi_legendre_eq_Pol_at_11,
   chi_legendre_eq_Pol_at_13,
   chi_legendre_eq_Pol_at_17,
   chi_legendre_eq_Pol_at_19,
   chi_legendre_eq_Pol_at_23⟩
```
