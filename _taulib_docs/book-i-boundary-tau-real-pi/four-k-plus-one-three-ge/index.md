---
{
  "projection_kind": "taulib_declaration",
  "title": "Nat.four_k_plus_one_three_ge",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/four-k-plus-one-three-ge/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealPi`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealPi::Nat.four_k_plus_one_three_ge",
  "declaration_slug": "four-k-plus-one-three-ge",
  "kind": "theorem",
  "name": "Nat.four_k_plus_one_three_ge",
  "module_name": "TauLib.BookI.Boundary.TauRealPi",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/",
  "source_line_start": 101,
  "source_line_end": 104,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L101-L104",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealPi",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-pi/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L101-L104",
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

- Module: [TauLib.BookI.Boundary.TauRealPi](/corpus/taulib/docs/book-i-boundary-tau-real-pi/)
- Source path: [`TauLib/BookI/Boundary/TauRealPi.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealPi.lean#L101-L104)
- Source range: L101-L104
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `(4k+1)(4k+3) ≥ 16 · k · (k+1)`, since
    `(4k+1)(4k+3) = 16k² + 16k + 3 = 16k(k+1) + 3`. -/
```

## Source Excerpt

```lean
theorem Nat.four_k_plus_one_three_ge (k : Nat) :
    16 * k * (k + 1) ≤ (4 * k + 1) * (4 * k + 3) := by
  have : (4 * k + 1) * (4 * k + 3) = 16 * k * (k + 1) + 3 := by ring
  omega
```
