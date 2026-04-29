---
{
  "projection_kind": "taulib_declaration",
  "title": "characteristic_morphism_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/characteristic-morphism-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::characteristic_morphism_witness",
  "declaration_slug": "characteristic-morphism-witness",
  "kind": "theorem",
  "name": "characteristic_morphism_witness",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 229,
  "source_line_end": 232,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L229-L232",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L229-L232",
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/verify/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L229-L232)
- Source range: L229-L232
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §4 Def `char-morphism` — characteristic morphism witness**.

    For any admissible-subobject predicate (modeled as B-membership
    + C-membership functions), the characteristic morphism χ_S
    sends each element to its Truth4 value (T/F/B/N) based on
    membership status.  The canonical existing
    `characteristic_morphism` is exactly this construction. -/
```

## Source Excerpt

```lean
theorem characteristic_morphism_witness
    (b_mem c_mem : TauIdx → Bool) :
    ∃ chi : TauIdx → Omega_tau, chi = characteristic_morphism b_mem c_mem :=
  ⟨characteristic_morphism b_mem c_mem, rfl⟩
```
