---
{
  "projection_kind": "taulib_declaration",
  "title": "terminal_level_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/terminal-level-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::terminal_level_check",
  "declaration_slug": "terminal-level-check",
  "kind": "def",
  "name": "terminal_level_check",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 127,
  "source_line_end": 141,
  "registry_ids": [
    "III.P31"
  ],
  "related_registry_items": [
    {
      "id": "III.P31",
      "title": "Terminal Level Characterization",
      "url": "/registry/object/III.P31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L127-L141",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L127-L141",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L127-L141)
- Source range: L127-L141
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P31` — Terminal Level Characterization

## Immediate Comment / Docstring

```lean
/-- [III.P31] Terminal level check: E3 is the maximum enrichment level.
    Verified by:
    1. E3.toNat = 3 (maximum index)
    2. EnrLevel.lt .E3 .E3 = false (not self-exceeding)
    3. E3.succ = E3 (successor saturates)
    4. The four levels [E0, E1, E2, E3] are exhaustive
    5. Applied saturation holds (E3 template is fixpoint) -/
```

## Source Excerpt

```lean
def terminal_level_check (bound db : TauIdx) : Bool :=
  -- E3 is maximal
  let max_level := EnrLevel.E3.toNat == 3
  -- E3 is not self-exceeding
  let not_self_exceeding := !EnrLevel.lt .E3 .E3
  -- Successor saturates
  let succ_saturates := EnrLevel.E3.succ == .E3
  -- Four levels are exhaustive
  let four_levels := [EnrLevel.E0, .E1, .E2, .E3].length == 4
  -- Applied saturation
  let saturated := applied_saturation_check bound db
  -- Full component-wise saturation
  let full_sat := full_saturation_check bound db
  max_level && not_self_exceeding && succ_saturates &&
    four_levels && saturated && full_sat
```
