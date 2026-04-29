---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L50",
  "permalink": "/verify/taulib/docs/tour-central-theorem/eval-l50/",
  "summary_short": "`eval` declaration in `TauLib.Tour.CentralTheorem`.",
  "declaration_id": "TauLib.Tour.CentralTheorem::#eval:50",
  "declaration_slug": "eval-l50",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.CentralTheorem",
  "module_url": "/verify/taulib/docs/tour-central-theorem/",
  "source_line_start": 50,
  "source_line_end": 68,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L50-L68",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.CentralTheorem",
        "url": "/verify/taulib/docs/tour-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L50-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.CentralTheorem](/verify/taulib/docs/tour-central-theorem/)
- Source path: [`TauLib/Tour/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/CentralTheorem.lean#L50-L68)
- Source range: L50-L68
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- The KEY difference from complex numbers: H has zero divisors!
-- (1+j)(1-j) = 0:
```

## Source Excerpt

```lean
#eval SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩       -- (0, 0)

-- This is not a bug — it is the structural origin of the B/C duality.
-- The zero divisors are exactly the elements with a vanishing sector.
#check zero_divisors_iff

-- H is a full commutative ring (all 8 axioms proved):
#check sc_ring_axioms

-- ================================================================
-- PART 2: SECTOR DECOMPOSITION — THE BIPOLAR SPLIT
-- ================================================================

-- The sector map phi : H -> Z x Z sends (a + bj) to (a+b, a-b).
-- This is a RING ISOMORPHISM to componentwise Z x Z.
-- The two components are the B-sector and C-sector.

#check to_sectors             -- SplitComplex -> SectorPair
#check from_sectors           -- SectorPair -> SplitComplex (left inverse)
```
