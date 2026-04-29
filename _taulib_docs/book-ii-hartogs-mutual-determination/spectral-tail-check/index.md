---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_tail_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/spectral-tail-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::spectral_tail_check",
  "declaration_slug": "spectral-tail-check",
  "kind": "def",
  "name": "spectral_tail_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 86,
  "source_line_end": 109,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L86-L109",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L86-L109",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L86-L109)
- Source range: L86-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.L02-L03, clause S] Spectral stabilization check:
    the B and C coordinates from from_tau_idx determine the spectral
    decomposition. At each stage k, the spectral content is determined
    by reduce(x, k), and once k is large enough, the B and C
    coordinates of from_tau_idx(reduce(x, k)) stabilize.

    We verify that the B-coordinate and C-coordinate of from_tau_idx
    applied to the stage-k reduction are well-defined and consistent:
    if reduce(x, k) = reduce(y, k), then the ABCD charts agree on
    the B and C coordinates at that resolution. -/
```

## Source Excerpt

```lean
def spectral_tail_check (bound db : TauIdx) : Bool :=
  go 2 2 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      -- Spectral stabilization: from_tau_idx applied to the stage-k reduction
      -- should be consistent across the tower.
      let rx := reduce x k
      let ry := reduce y k
      -- (1) Agreement: same reduced value → same spectral data
      let agree_ok := !(rx == ry) ||
        ((from_tau_idx rx).b == (from_tau_idx ry).b &&
         (from_tau_idx rx).c == (from_tau_idx ry).c)
      -- (2) Non-degeneracy: from_tau_idx(reduce(x,k)) round-trips through
      --     the ABCD chart (exercises from_tau_idx + reduce on distinct paths)
      let p := from_tau_idx rx
      let chart_sum := p.a + p.b + p.c + p.d
      let nondegen_ok := rx < 2 || chart_sum > 0
      agree_ok && nondegen_ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
