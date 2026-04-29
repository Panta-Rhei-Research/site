---
{
  "projection_kind": "taulib_declaration",
  "title": "Nat.two_pow_succ_gt_linear",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/two-pow-succ-gt-linear/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Nat.two_pow_succ_gt_linear",
  "declaration_slug": "two-pow-succ-gt-linear",
  "kind": "theorem",
  "name": "Nat.two_pow_succ_gt_linear",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 80,
  "source_line_end": 85,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L80-L85",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L80-L85",
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

- Module: [TauLib.BookI.Boundary.TauRealAnalyticalHelpers](/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/)
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L80-L85)
- Source range: L80-L85
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `k + 1 < 2^(k+1)` at the Nat level. -/
```

## Source Excerpt

```lean
theorem Nat.two_pow_succ_gt_linear (k : Nat) : k + 1 < 2 ^ (k + 1) := by
  induction k with
  | zero => norm_num
  | succ k ih =>
    have h_ring : 2 ^ (k + 1 + 1) = 2 * 2 ^ (k + 1) := by ring
    linarith
```
