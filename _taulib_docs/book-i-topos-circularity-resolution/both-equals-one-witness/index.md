---
{
  "projection_kind": "taulib_declaration",
  "title": "both_equals_one_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-one-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::both_equals_one_witness",
  "declaration_slug": "both-equals-one-witness",
  "kind": "theorem",
  "name": "both_equals_one_witness",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 400,
  "source_line_end": 404,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L400-L404",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L400-L404",
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
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L400-L404)
- Source range: L400-L404
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Per the paper's `both-equals-one-id`, the algebraic content
    of the Liar's ω-germ stabilisation is precisely the
    sector-sum identity `e_+ + e_- = 1`, which on the Truth4
    encoding is exposed by `Logic.Explosion.spectral_bridge_partition`
    (`Truth4.toSectorPair B + Truth4.toSectorPair N = Truth4.toSectorPair T`).

    The Liar lands at `B` (the apex of the diamond lattice);
    `B`'s sector-pair encoding is `e_+ = (1, 0)`, and `B + N` (its
    diamond complement) sums to the top.  This Lean rendering
    therefore exposes *two* algebraic identities that the paper's
    "Both = 1" proof depends on:

      (i)  the lobe-pair sum  `T-sector + F-sector = T-sector` (here),
      (ii) the diamond-pair sum `B-sector + N-sector = T-sector`
           (already in `Logic.Explosion.spectral_bridge_partition`).

    Together they witness the four-atom partition-of-unity in
    `B_σ` from which the Hinge 4 uniqueness theorem on `D` is
    inherited. -/
```

## Source Excerpt

```lean
theorem both_equals_one_witness :
    Tau.Polarity.SectorPair.add
      (Truth4.toSectorPair B) (Truth4.toSectorPair N) =
    Truth4.toSectorPair T :=
  Tau.Logic.spectral_bridge_partition
```
