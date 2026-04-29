---
{
  "projection_kind": "taulib_declaration",
  "title": "double_neg_mod",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/double-neg-mod/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::double_neg_mod",
  "declaration_slug": "double-neg-mod",
  "kind": "theorem",
  "name": "double_neg_mod",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 201,
  "source_line_end": 211,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L201-L211",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/verify/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L201-L211",
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

- Module: [TauLib.BookI.Boundary.Ring](/verify/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L201-L211)
- Source range: L201-L211
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Double negation on Nat mod: (M - (M - x%M)%M) % M = x%M. -/
```

## Source Excerpt

```lean
private theorem double_neg_mod (x M : Nat) (hM : M > 0) :
    (M - (M - x % M) % M) % M = x % M := by
  have hxm : x % M < M := Nat.mod_lt x hM
  by_cases h0 : x % M = 0
  · rw [h0, Nat.sub_zero, Nat.mod_self, Nat.sub_zero, Nat.mod_self]
  · have hpos : x % M > 0 := Nat.pos_of_ne_zero h0
    have h1 : M - x % M < M := by omega
    rw [Nat.mod_eq_of_lt h1]
    have h2 : M - (M - x % M) = x % M := by omega
    rw [h2]
    exact Nat.mod_eq_of_lt hxm
```
