---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.two_approx_toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/two-approx-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealIotaTau`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealIotaTau::TauReal.two_approx_toRat",
  "declaration_slug": "two-approx-to-rat",
  "kind": "theorem",
  "name": "TauReal.two_approx_toRat",
  "module_name": "TauLib.BookI.Boundary.TauRealIotaTau",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/",
  "source_line_start": 81,
  "source_line_end": 85,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L81-L85",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealIotaTau",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L81-L85",
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

- Module: [TauLib.BookI.Boundary.TauRealIotaTau](/verify/taulib/docs/book-i-boundary-tau-real-iota-tau/)
- Source path: [`TauLib/BookI/Boundary/TauRealIotaTau.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealIotaTau.lean#L81-L85)
- Source range: L81-L85
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `TauReal.two.approx n = 2` at toRat level, for every `n`. -/
```

## Source Excerpt

```lean
theorem TauReal.two_approx_toRat (n : Nat) :
    (TauReal.two.approx n).toRat = 2 := by
  show (({ num := ⟨2, 0⟩, den := 1, den_pos := Nat.one_pos } : TauRat).toRat) = 2
  unfold TauRat.toRat TauInt.toInt
  push_cast; ring
```
