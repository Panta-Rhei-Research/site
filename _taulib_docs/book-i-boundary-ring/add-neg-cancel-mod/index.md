---
{
  "projection_kind": "taulib_declaration",
  "title": "add_neg_cancel_mod",
  "permalink": "/corpus/taulib/docs/book-i-boundary-ring/add-neg-cancel-mod/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::add_neg_cancel_mod",
  "declaration_slug": "add-neg-cancel-mod",
  "kind": "theorem",
  "name": "add_neg_cancel_mod",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/corpus/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 232,
  "source_line_end": 242,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L232-L242",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/corpus/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L232-L242",
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

- Module: [TauLib.BookI.Boundary.Ring](/corpus/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L232-L242)
- Source range: L232-L242
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- x + (M - x%M)%M = 0 (mod M). -/
```

## Source Excerpt

```lean
private theorem add_neg_cancel_mod (x M : Nat) (hM : M > 0) :
    (x % M + (M - x % M) % M) % M = 0 := by
  have hxm : x % M < M := Nat.mod_lt x hM
  by_cases h0 : x % M = 0
  · rw [h0, Nat.sub_zero, Nat.mod_self, Nat.add_zero, Nat.zero_mod]
  · have hpos : x % M > 0 := Nat.pos_of_ne_zero h0
    have h1 : M - x % M < M := by omega
    rw [Nat.mod_eq_of_lt h1]
    have h2 : x % M + (M - x % M) = M := by omega
    rw [h2]
    exact Nat.mod_self M
```
