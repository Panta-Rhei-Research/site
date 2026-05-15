---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.ofRat_toRat",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/of-rat-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.ofRat_toRat",
  "declaration_slug": "of-rat-to-rat",
  "kind": "theorem",
  "name": "TauRatQ.ofRat_toRat",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 384,
  "source_line_end": 391,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L384-L391",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L384-L391",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L384-L391)
- Source range: L384-L391
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem TauRatQ.ofRat_toRat (q : Rat) : (TauRatQ.ofRat q).toRat = q := by
  unfold TauRatQ.ofRat
  simp only [TauRatQ.toRat_mk]
  unfold TauRat.toRat TauInt.toInt
  -- Goal: ↑((q.num.toNat : Int) - ((-q.num).toNat : Int)) / ↑q.den = q
  have h_int : (q.num.toNat : Int) - ((-q.num).toNat : Int) = q.num := by omega
  rw [h_int]
  exact Rat.num_div_den q
```
