---
{
  "projection_kind": "taulib_declaration",
  "title": "gluing_lemma_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/gluing-lemma-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::gluing_lemma_check",
  "declaration_slug": "gluing-lemma-check",
  "kind": "def",
  "name": "gluing_lemma_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 218,
  "source_line_end": 240,
  "registry_ids": [
    "II.L06"
  ],
  "related_registry_items": [
    {
      "id": "II.L06",
      "title": "Gluing Lemma",
      "url": "/registry/object/II.L06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L218-L240",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L218-L240",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L218-L240)
- Source range: L218-L240
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L06` — Gluing Lemma

## Immediate Comment / Docstring

```lean
/-- [II.L06] Gluing Lemma: local functions on disjoint cylinders paste
    to a global function.

    In the ultrametric setting, same-stage cylinders are disjoint, so
    gluing is simply concatenation. We verify: given a family of values
    (one per cylinder at stage k), the "pasted" function f(x) = val(a)
    where a = reduce(x,k) is well-defined and restricts correctly.

    The test uses f(x) = reduce(x, k) as the "local section" for cylinder
    C_{k, reduce(x,k)}, and checks that the pasted function equals the
    global reduce. -/
```

## Source Excerpt

```lean
def gluing_lemma_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 300 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let pk := primorial k
      -- Paste: for each x in [0, P_k), the glued value is reduce(x, k)
      -- This IS the canonical section, and it equals x for x < P_k
      let ok := check_paste 0 pk k
      -- Disjointness: all same-stage cylinders are disjoint
      let disj := batch_disjoint_check k
      ok && disj && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_paste (x fuel k : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      -- reduce(x, k) = x for x < P_k (since x < P_k)
      let rx := reduce x k
      (rx == x) && check_paste (x + 1) (fuel - 1) k
  termination_by fuel
```
