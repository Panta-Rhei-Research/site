---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/hartogs-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::hartogs_uniqueness_check",
  "declaration_slug": "hartogs-uniqueness-check",
  "kind": "def",
  "name": "hartogs_uniqueness_check",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 149,
  "source_line_end": 170,
  "registry_ids": [
    "II.T37"
  ],
  "related_registry_items": [
    {
      "id": "II.T37",
      "title": "Hartogs Extension Uniqueness",
      "url": "/registry/object/II.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L149-L170",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L149-L170",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L149-L170)
- Source range: L149-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T37] Hartogs uniqueness check: for test functions, verify that
    two different extensions from the same boundary data give the same result.

    The "two extensions" are:
    1. Direct bndlift: bndlift(x, k) = reduce(x, k+1)
    2. Alternative: reduce(bndlift(x, k+1), k) (lift one stage further, then reduce back)

    Both must agree at stage k by tower coherence. -/
```

## Source Excerpt

```lean
def hartogs_uniqueness_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k + 1 >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Extension 1: direct at stage k
      let ext1 := bndlift x k
      -- Extension 2: lift to stage k+1, then reduce back to k
      let ext2_lifted := bndlift x (k + 1)
      let ext2 := reduce ext2_lifted k
      -- Stage-k data from extension 1
      let r1 := reduce ext1 k
      -- Both should give the same stage-k value
      let ok := r1 == ext2
      -- Also check that both reduce to the same stage-k value as the original
      let orig_k := reduce x k
      let ok2 := r1 == orig_k && ext2 == orig_k
      ok && ok2 && go x (k + 1) (fuel - 1)
  termination_by fuel
```
