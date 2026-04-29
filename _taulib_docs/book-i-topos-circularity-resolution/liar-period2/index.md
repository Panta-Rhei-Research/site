---
{
  "projection_kind": "taulib_declaration",
  "title": "liar_period2",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/liar-period2/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::liar_period2",
  "declaration_slug": "liar-period2",
  "kind": "theorem",
  "name": "liar_period2",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 228,
  "source_line_end": 244,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L228-L244",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L228-L244",
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
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L228-L244)
- Source range: L228-L244
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Liar iteration is **period-2 on lobes** from seed `F`. -/
```

## Source Excerpt

```lean
theorem liar_period2 : Period2OnLobes liarTemplate F := by
  refine ⟨0, fun n _ => ?_⟩
  rw [liar_iter_alternates n, liar_iter_alternates (n + 1)]
  by_cases hn : n % 2 = 0
  · -- n even: iter n = F, iter (n+1) = T → right disjunct
    rw [if_pos hn]
    have h_succ : (n + 1) % 2 = 1 := by omega
    rw [if_neg (by omega)]
    right
    exact ⟨rfl, rfl⟩
  · -- n odd: iter n = T, iter (n+1) = F → left disjunct
    rw [if_neg hn]
    have hn' : n % 2 = 1 := by omega
    have h_succ : (n + 1) % 2 = 0 := by omega
    rw [if_pos h_succ]
    left
    exact ⟨rfl, rfl⟩
```
