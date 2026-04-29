---
{
  "projection_kind": "taulib_declaration",
  "title": "yoneda_bipolar_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/yoneda-bipolar-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.YonedaTheorem`.",
  "declaration_id": "TauLib.BookII.Enrichment.YonedaTheorem::yoneda_bipolar_check",
  "declaration_slug": "yoneda-bipolar-check",
  "kind": "def",
  "name": "yoneda_bipolar_check",
  "module_name": "TauLib.BookII.Enrichment.YonedaTheorem",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/",
  "source_line_start": 176,
  "source_line_end": 204,
  "registry_ids": [
    "II.T36"
  ],
  "related_registry_items": [
    {
      "id": "II.T36",
      "title": "Tau-Yoneda Embedding",
      "url": "/registry/object/II.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L176-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.YonedaTheorem",
        "url": "/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L176-L204",
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

- Module: [TauLib.BookII.Enrichment.YonedaTheorem](/verify/taulib/docs/book-ii-enrichment-yoneda-theorem/)
- Source path: [`TauLib/BookII/Enrichment/YonedaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/YonedaTheorem.lean#L176-L204)
- Source range: L176-L204
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T36` — Tau-Yoneda Embedding

## Immediate Comment / Docstring

```lean
/-- [II.T36] Yoneda bipolar preservation:
    The pre-Yoneda embedding preserves bipolar decomposition.
    The B-channel of y(f) comes from the B-projection of f,
    and the C-channel from the C-projection.

    Concretely: the sector pair of preyoneda(f, x, k) decomposes
    into e_plus and e_minus projections that are independently
    determined by the B-data and C-data of f's output.

    Verified: for f = identity, the bipolar decomposition of
    f(reduce(x, k)) decomposes correctly. -/
```

## Source Excerpt

```lean
def yoneda_bipolar_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Embed the identity: preyoneda(id, x, k) = reduce(x, k)
      let embedded := reduce x k
      let p := from_tau_idx embedded
      let sp := interior_bipolar p
      -- B-channel projection
      let proj_b := SectorPair.mul e_plus_sector sp
      -- C-channel projection
      let proj_c := SectorPair.mul e_minus_sector sp
      -- Completeness: projections recombine
      let recombined := SectorPair.add proj_b proj_c
      let complete_ok := recombined == sp
      -- The B-channel value is determined by the B-coordinate of the point
      let b_val := proj_b.b_sector
      let b_expected := (p.b : Int)
      let b_ok := b_val == b_expected
      -- The C-channel value is determined by the C-coordinate of the point
      let c_val := proj_c.c_sector
      let c_expected := (p.c : Int)
      let c_ok := c_val == c_expected
      complete_ok && b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
