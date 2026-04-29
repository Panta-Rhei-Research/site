---
{
  "projection_kind": "taulib_declaration",
  "title": "liar_iter_alternates",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-iter-alternates/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::liar_iter_alternates",
  "declaration_slug": "liar-iter-alternates",
  "kind": "theorem",
  "name": "liar_iter_alternates",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 208,
  "source_line_end": 225,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L208-L225",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L208-L225",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L208-L225)
- Source range: L208-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Liar iteration from seed `F` alternates `F, T, F, T, …`. -/
```

## Source Excerpt

```lean
theorem liar_iter_alternates (n : Nat) :
    cauchyIter liarTemplate n F = (if n % 2 = 0 then F else T) := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [cauchyIter_succ, ih]
    by_cases hk : k % 2 = 0
    · -- k even ⇒ iter k = F, iter (k+1) = σ F = T
      rw [if_pos hk]
      have h_succ : (k + 1) % 2 = 1 := by omega
      rw [if_neg (by omega)]
      rfl
    · -- k odd ⇒ iter k = T, iter (k+1) = σ T = F
      rw [if_neg hk]
      have hk' : k % 2 = 1 := by omega
      have h_succ : (k + 1) % 2 = 0 := by omega
      rw [if_pos h_succ]
      rfl
```
