---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_necessary_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/bridge-necessary-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::bridge_necessary_check",
  "declaration_slug": "bridge-necessary-check",
  "kind": "def",
  "name": "bridge_necessary_check",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 193,
  "source_line_end": 198,
  "registry_ids": [
    "III.T80"
  ],
  "related_registry_items": [
    {
      "id": "III.T80",
      "title": "Bridge Necessary Insufficient",
      "url": "/registry/object/III.T80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L193-L198",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L193-L198",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L193-L198)
- Source range: L193-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T80` — Bridge Necessary Insufficient

## Immediate Comment / Docstring

```lean
/-- [III.T80] Bridge is necessary: all three conjectures have status
    "conjectural" or lower in the bridge taxonomy. Without the bridge,
    τ-internal results cannot make claims about ℕ-level conjectures.
    The bridge is necessary but NOT sufficient (even with bridge, the
    analytic component is missing). -/
```

## Source Excerpt

```lean
def bridge_necessary_check : Bool :=
  let fm_ok := all_conjectures.all (fun c =>
    gap_forbidden_move c == ForbiddenMove.exponential_quantification)
  let distinct := (all_conjectures.map (fun c => (conjecture_gap_type c).toNat)).eraseDups.length == 3
  let damage_ok := bridge_damage ForbiddenMove.exponential_quantification == 3
  fm_ok && distinct && damage_ok
```
