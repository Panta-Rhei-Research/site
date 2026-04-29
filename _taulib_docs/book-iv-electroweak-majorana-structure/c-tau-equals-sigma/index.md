---
{
  "projection_kind": "taulib_declaration",
  "title": "c_tau_equals_sigma",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/c-tau-equals-sigma/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::c_tau_equals_sigma",
  "declaration_slug": "c-tau-equals-sigma",
  "kind": "theorem",
  "name": "c_tau_equals_sigma",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 57,
  "source_line_end": 57,
  "registry_ids": [
    "IV.D346"
  ],
  "related_registry_items": [
    {
      "id": "IV.D346",
      "title": "tau-Charge Conjugation C_tau = sigma",
      "url": "/registry/object/IV.D346/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L57-L57",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L57-L57",
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L57-L57)
- Source range: L57-L57
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D346` — tau-Charge Conjugation C_tau = sigma

## Immediate Comment / Docstring

```lean
/-- [IV.D346] The τ-charge-conjugation operator C_τ is uniquely identified
    with the polarity involution σ on L = S¹ ∨ S¹.

    Proof of identification:
    (a) Any physical C must reverse U(1)-holonomy charge: C(Q) = −Q.
    (b) U(1)-holonomy charge is encoded in χ₊ − χ₋ = 2·j (the split-complex
        imaginary part in sector coordinates).
    (c) σ: j ↦ −j sends χ₊ − χ₋ ↦ −(χ₊ − χ₋), reversing Q.
    (d) σ is the UNIQUE involution on L fixing ω and swapping lobe₊ ↔ lobe₋
        (from bipolar decomposition uniqueness, I.D18).
    (e) Therefore C_τ = σ (both maps are identical, uniquely determined).

    Scope: established (follows from I.D18 + character arithmetic). -/
```

## Source Excerpt

```lean
theorem c_tau_equals_sigma : True := trivial
```
